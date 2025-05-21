import os
from google.cloud import texttospeech
from gtts import gTTS
import ffmpeg

class AudioGenerator:
    def __init__(self):
        self.client = texttospeech.TextToSpeechClient()
        
    def generate_audio(self, text: str, language_code: str, output_dir: str) -> str:
        """
        Generate audio from text using Google Cloud Text-to-Speech.
        
        Args:
            text: Text to convert to speech
            language_code: Language code for speech synthesis
            output_dir: Directory to save the audio file
            
        Returns:
            Path to the generated audio file
        """
        try:
            # Set up the voice
            voice = texttospeech.VoiceSelectionParams(
                language_code=language_code,
                ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
            )
            
            # Set up the audio configuration
            audio_config = texttospeech.AudioConfig(
                audio_encoding=texttospeech.AudioEncoding.MP3
            )
            
            # Generate speech
            synthesis_input = texttospeech.SynthesisInput(text=text)
            response = self.client.synthesize_speech(
                input=synthesis_input,
                voice=voice,
                audio_config=audio_config
            )
            
            # Save the audio file
            output_path = os.path.join(output_dir, 'summary.mp3')
            with open(output_path, 'wb') as out:
                out.write(response.audio_content)
                
            return output_path
            
        except Exception as e:
            # Fallback to gTTS if Google Cloud fails
            return self._generate_audio_gtts(text, language_code, output_dir)
            
    def _generate_audio_gtts(self, text: str, language_code: str, output_dir: str) -> str:
        """
        Generate audio from text using gTTS (fallback method).
        
        Args:
            text: Text to convert to speech
            language_code: Language code for speech synthesis
            output_dir: Directory to save the audio file
            
        Returns:
            Path to the generated audio file
        """
        try:
            # Create gTTS object
            tts = gTTS(text=text, lang=language_code[:2])
            
            # Save the audio file
            output_path = os.path.join(output_dir, 'summary.mp3')
            tts.save(output_path)
            
            return output_path
            
        except Exception as e:
            raise Exception(f"Error generating audio with gTTS: {str(e)}")
            
    def create_video_summary(self, video_path: str, summary_audio_path: str, output_dir: str) -> str:
        """
        Create a video summary by combining key frames with audio.
        
        Args:
            video_path: Path to the original video
            summary_audio_path: Path to the summary audio
            output_dir: Directory to save the output video
            
        Returns:
            Path to the generated video summary
        """
        try:
            output_path = os.path.join(output_dir, 'summary.mp4')
            
            # Get video information
            probe = ffmpeg.probe(video_path)
            video_info = next(s for s in probe['streams'] if s['codec_type'] == 'video')
            
            # Create video stream from key frames
            video_stream = ffmpeg.input(video_path)
            
            # Create audio stream from summary
            audio_stream = ffmpeg.input(summary_audio_path)
            
            # Combine video and audio
            stream = ffmpeg.output(
                video_stream,
                audio_stream,
                output_path,
                vcodec='libx264',
                acodec='aac',
                strict='experimental'
            )
            
            # Run ffmpeg
            ffmpeg.run(stream, overwrite_output=True)
            
            return output_path
            
        except Exception as e:
            raise Exception(f"Error creating video summary: {str(e)}")
            
    def adjust_audio_speed(self, audio_path: str, speed_factor: float, output_dir: str) -> str:
        """
        Adjust the speed of an audio file.
        
        Args:
            audio_path: Path to the audio file
            speed_factor: Speed adjustment factor (e.g., 1.5 for 50% faster)
            output_dir: Directory to save the modified audio
            
        Returns:
            Path to the modified audio file
        """
        try:
            output_path = os.path.join(output_dir, 'adjusted_audio.mp3')
            
            # Adjust audio speed using ffmpeg
            stream = ffmpeg.input(audio_path)
            stream = ffmpeg.output(
                stream,
                output_path,
                af=f'atempo={speed_factor}'
            )
            
            # Run ffmpeg
            ffmpeg.run(stream, overwrite_output=True)
            
            return output_path
            
        except Exception as e:
            raise Exception(f"Error adjusting audio speed: {str(e)}") 
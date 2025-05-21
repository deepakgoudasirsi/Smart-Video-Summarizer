import os
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types
import ffmpeg

class TranscriptionService:
    def __init__(self):
        self.client = speech.SpeechClient()
        
    def transcribe(self, video_path: str, language_code: str = 'en-US') -> str:
        """
        Transcribe audio from video file using Google Cloud Speech-to-Text.
        
        Args:
            video_path: Path to the video file
            language_code: Language code for transcription
            
        Returns:
            Transcribed text
        """
        try:
            # Extract audio from video
            audio_path = self._extract_audio(video_path)
            
            # Read audio file
            with open(audio_path, 'rb') as audio_file:
                content = audio_file.read()
            
            # Configure audio
            audio = types.RecognitionAudio(content=content)
            config = types.RecognitionConfig(
                encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
                sample_rate_hertz=16000,
                language_code=language_code,
                enable_automatic_punctuation=True,
                enable_word_time_offsets=True
            )
            
            # Perform transcription
            response = self.client.recognize(config=config, audio=audio)
            
            # Combine transcriptions
            transcript = ''
            for result in response.results:
                transcript += result.alternatives[0].transcript + ' '
            
            # Clean up temporary audio file
            os.remove(audio_path)
            
            return transcript.strip()
            
        except Exception as e:
            raise Exception(f"Error transcribing audio: {str(e)}")
            
    def _extract_audio(self, video_path: str) -> str:
        """
        Extract audio from video file using ffmpeg.
        
        Args:
            video_path: Path to the video file
            
        Returns:
            Path to the extracted audio file
        """
        audio_path = video_path.rsplit('.', 1)[0] + '.wav'
        
        try:
            # Extract audio using ffmpeg
            stream = ffmpeg.input(video_path)
            stream = ffmpeg.output(stream, audio_path, acodec='pcm_s16le', ac=1, ar='16k')
            ffmpeg.run(stream, overwrite_output=True)
            
            return audio_path
            
        except Exception as e:
            raise Exception(f"Error extracting audio: {str(e)}")
            
    def get_word_timestamps(self, video_path: str, language_code: str = 'en-US') -> list:
        """
        Get word-level timestamps from video.
        
        Args:
            video_path: Path to the video file
            language_code: Language code for transcription
            
        Returns:
            List of tuples containing (word, start_time, end_time)
        """
        try:
            # Extract audio from video
            audio_path = self._extract_audio(video_path)
            
            # Read audio file
            with open(audio_path, 'rb') as audio_file:
                content = audio_file.read()
            
            # Configure audio
            audio = types.RecognitionAudio(content=content)
            config = types.RecognitionConfig(
                encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
                sample_rate_hertz=16000,
                language_code=language_code,
                enable_word_time_offsets=True
            )
            
            # Perform transcription
            response = self.client.recognize(config=config, audio=audio)
            
            # Extract word timestamps
            word_timestamps = []
            for result in response.results:
                for word_info in result.alternatives[0].words:
                    word = word_info.word
                    start_time = word_info.start_time.seconds + word_info.start_time.nanos * 1e-9
                    end_time = word_info.end_time.seconds + word_info.end_time.nanos * 1e-9
                    word_timestamps.append((word, start_time, end_time))
            
            # Clean up temporary audio file
            os.remove(audio_path)
            
            return word_timestamps
            
        except Exception as e:
            raise Exception(f"Error getting word timestamps: {str(e)}") 
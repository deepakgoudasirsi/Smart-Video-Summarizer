import os
import argparse
from dotenv import load_dotenv
from src.video_processor import VideoProcessor
from src.transcription import TranscriptionService
from src.summarizer import VideoSummarizer
from src.audio_generator import AudioGenerator
from src.visualization import Visualizer
from src.sentiment_analyzer import SentimentAnalyzer

def main():
    # Load environment variables
    load_dotenv()
    
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Smart Video Summarizer')
    parser.add_argument('--input', required=True, help='Input video file path or URL')
    parser.add_argument('--output_dir', default='data/output', help='Output directory for summaries')
    parser.add_argument('--language', default='en-US', help='Language code for transcription')
    parser.add_argument('--format', choices=['text', 'audio', 'video'], default='text',
                      help='Output format for summary')
    args = parser.parse_args()

    # Create output directory if it doesn't exist
    os.makedirs(args.output_dir, exist_ok=True)

    try:
        # Initialize components
        video_processor = VideoProcessor()
        transcription_service = TranscriptionService()
        summarizer = VideoSummarizer()
        audio_generator = AudioGenerator()
        visualizer = Visualizer()
        sentiment_analyzer = SentimentAnalyzer()

        # Process video
        print("Processing video...")
        frames = video_processor.process_video(args.input)
        
        # Generate transcription
        print("Generating transcription...")
        transcription = transcription_service.transcribe(args.input, args.language)
        
        # Generate summary
        print("Generating summary...")
        summary = summarizer.summarize(transcription)
        
        # Analyze sentiment
        print("Analyzing sentiment...")
        sentiment = sentiment_analyzer.analyze(transcription)
        
        # Generate visualizations
        print("Generating visualizations...")
        visualizer.create_visualizations(frames, sentiment, args.output_dir)
        
        # Generate audio summary if requested
        if args.format in ['audio', 'video']:
            print("Generating audio summary...")
            audio_path = audio_generator.generate_audio(summary, args.language, args.output_dir)
        
        # Save summary
        output_path = os.path.join(args.output_dir, 'summary.txt')
        with open(output_path, 'w') as f:
            f.write(summary)
        
        print(f"Summary saved to: {output_path}")
        
    except Exception as e:
        print(f"Error processing video: {str(e)}")
        raise

if __name__ == "__main__":
    main() 
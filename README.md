# Smart Video Summarizer 🎥

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.12.0-orange)](https://www.tensorflow.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.7.0-blue)](https://opencv.org/)

Smart Video Summarizer is an AI-powered tool designed to analyze and summarize healthcare videos, such as surgery recordings and patient health data, enabling healthcare professionals to quickly access critical insights without watching the entire video.

## 📋 Overview

This project leverages advanced AI and machine learning techniques to process healthcare videos, extract meaningful information, and generate concise summaries. It's particularly useful for medical professionals who need to quickly review surgical procedures, patient consultations, or medical training videos.

## 🛠️ Tech Stack

### Core Technologies
- **Python 3.8+**: Primary programming language
- **TensorFlow**: Deep learning framework for video analysis
- **OpenCV**: Video processing and computer vision
- **Google Cloud APIs**: Speech-to-Text and Text-to-Speech services
- **FFmpeg**: Video processing and manipulation

### AI/ML Components
- **Transformers**: Natural language processing for summarization
- **scikit-learn**: Machine learning algorithms for analysis
- **PyTorch**: Deep learning framework for advanced models

### Data Processing
- **NumPy**: Numerical computing
- **Pandas**: Data manipulation and analysis
- **Matplotlib & Seaborn**: Data visualization

### Audio Processing
- **gTTS**: Google Text-to-Speech integration
- **FFmpeg-python**: Audio processing and conversion

## Features

- Video Upload: Upload videos from various sources (URLs, local files, cloud storage)
- Transcription: Converts spoken content in videos into text using Google Speech-to-Text API
- Text-to-Audio: Converts text summaries into audio using Google Text-to-Speech
- Summarization: Automatically generates concise video summaries based on important events
- Multi-Language Support: Handles multiple languages for transcription and summarization
- Visualization & Analytics: Provides visualizations for engagement and summary effectiveness
- Sentiment Analysis: Analyzes the emotional tone of video content
- Download Options: Download summaries as text, audio, or video clips
- AI-Powered Recommendations: Suggests related content based on user interactions

## Prerequisites

- Python 3.8 or higher
- FFmpeg installed on your system
- Google Cloud account with Speech-to-Text and Text-to-Speech APIs enabled

## 📸 Screenshots

### Video Processing Interface
![Video Processing](screenshots/video_processing.png)

### Summary Generation
![Summary Generation](screenshots/summary_generation.png)

### Analytics Dashboard
![Analytics Dashboard](screenshots/analytics_dashboard.png)

*Note: Screenshots will be added once the UI is implemented*

## 🚀 Quick Start

1. Clone the repository:
```bash
git clone https://github.com/yourusername/smart-video-summarizer.git
cd smart-video-summarizer
```

2. Set up the environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. Configure Google Cloud credentials:
```bash
export GOOGLE_APPLICATION_CREDENTIALS="path/to/your/credentials.json"
```

4. Run the application:
```bash
python main.py --input path/to/your/video.mp4 --output_dir path/to/output
```

## Command Line Arguments

- `--input`: Path to the input video file (required)
- `--output_dir`: Directory to save the output files (default: 'data/output')
- `--language`: Language code for transcription (default: 'en-US')
- `--format`: Output format for summary (choices: 'text', 'audio', 'video', default: 'text')

## Output

The tool generates the following outputs in the specified output directory:

1. `summary.txt`: Text summary of the video
2. `summary.mp3`: Audio summary (if audio format is selected)
3. `summary.mp4`: Video summary (if video format is selected)
4. `sentiment_timeline.png`: Visualization of sentiment analysis
5. `frame_analysis.png`: Analysis of video frames
6. `summary_visualization.png`: Comprehensive summary visualization

## Supported Languages

The tool supports all languages available in Google Cloud Speech-to-Text API, including:

- English (en-US, en-GB)
- Spanish (es-ES, es-MX)
- French (fr-FR)
- German (de-DE)
- Italian (it-IT)
- Japanese (ja-JP)
- Korean (ko-KR)
- Chinese (zh-CN, zh-TW)
- And many more...

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Google Cloud Speech-to-Text API
- Google Cloud Text-to-Speech API
- Hugging Face Transformers
- FFmpeg
- OpenCV
- Matplotlib and Seaborn

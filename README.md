# Smart Video Summarizer - Project Explanation

## 📊 Project Overview

The **Smart Video Summarizer** is an AI-powered tool specifically designed for healthcare professionals to quickly analyze and understand video content, such as surgery recordings and patient consultations, without having to watch the entire video.

## ✨ Key Features

### 1. Intelligent Video Processing

* Extracts key frames from videos
* Detects scene changes
* Analyzes visual content using computer vision (OpenCV)

### 2. Advanced Speech Recognition

* Converts spoken content to text using Google Cloud Speech-to-Text
* Supports multiple languages
* Provides word-level timestamps for precise analysis

### 3. AI-Powered Summarization

* Uses the BART model from Hugging Face Transformers
* Generates concise summaries of video content
* Extracts key points and important events

### 4. Sentiment Analysis

* Analyzes emotional tone of the content
* Provides sentiment scores over time
* Identifies key emotional moments

### 5. Visualization & Analytics

* Creates timeline visualizations
* Generates frame analysis graphs
* Provides comprehensive summary visualizations

### 6. Multi-Format Output

* Text summaries
* Audio summaries
* Video summaries with key moments

## 📈 Technical Architecture

### Core Components

* `video_processor.py`: Handles video processing and frame extraction
* `transcription.py`: Manages speech-to-text conversion
* `summarizer.py`: Generates concise summaries using NLP
* `audio_generator.py`: Converts text summaries into speech
* `sentiment_analyzer.py`: Performs sentiment analysis on transcript
* `visualization.py`: Creates graphs and visual representations


## 🚀 Use Cases

### Medical Education

* Summarize surgical procedures
* Extract key learning points from lectures
* Create concise video tutorials

### Patient Care

* Review consultations quickly
* Identify key moments in interactions
* Generate documentation for medical records

### Research & Analysis

* Analyze patterns in procedures
* Study communication in healthcare
* Gain insights from training content

## ⚙️ How It Works

### Input Processing

```bash
python main.py --input video.mp4 --output_dir output
```

### Processing Pipeline

* Frames extracted and analyzed with OpenCV
* Audio transcribed using Google Cloud Speech API
* Summarization via Hugging Face Transformers
* Sentiment analysis on transcript
* Visualizations created with matplotlib/seaborn

### Output Files

* `summary.txt`: Text summary
* `summary.mp3`: Audio summary (optional)
* `summary.mp4`: Video summary (optional)
* `sentiment_timeline.png`: Sentiment analysis
* `frame_analysis.png`: Frame analysis
* `summary_visualization.png`: Summary visualization

---

## Benefits

* Saves 80-90% time on video review
* Helps healthcare professionals quickly find critical information
* Supports better documentation and medical training

---

### Installation

```bash
# Clone repository
git clone https://github.com/deepakgoudasirsi/smart-video-summarizer.git
cd smart-video-summarizer

```
---

## Contact

* **Deepak Gouda**
  [GitHub @deepakgoudasirsi](https://github.com/deepakgoudasirsi)
  [LinkedIn: Deepak Gouda](https://linkedin.com/in/deepakgoudasirsi)


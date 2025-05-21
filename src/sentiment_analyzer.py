from transformers import pipeline
from typing import Dict, List
import numpy as np

class SentimentAnalyzer:
    def __init__(self):
        # Initialize the sentiment analysis pipeline
        self.analyzer = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
        
    def analyze(self, text: str) -> Dict[str, float]:
        """
        Analyze sentiment of the input text.
        
        Args:
            text: Input text to analyze
            
        Returns:
            Dictionary containing sentiment scores
        """
        try:
            # Split text into sentences
            sentences = self._split_into_sentences(text)
            
            # Analyze sentiment for each sentence
            sentiment_scores = {}
            for i, sentence in enumerate(sentences):
                result = self.analyzer(sentence)[0]
                # Convert label to score (-1 to 1)
                score = 1 if result['label'] == 'POSITIVE' else -1
                score *= result['score']  # Weight by confidence
                sentiment_scores[i] = score
                
            return sentiment_scores
            
        except Exception as e:
            raise Exception(f"Error analyzing sentiment: {str(e)}")
            
    def _split_into_sentences(self, text: str) -> List[str]:
        """
        Split text into sentences.
        
        Args:
            text: Input text
            
        Returns:
            List of sentences
        """
        # Simple sentence splitting by period
        sentences = [s.strip() for s in text.split('.') if s.strip()]
        return sentences
        
    def analyze_timeline(self, text: str, timestamps: List[tuple]) -> Dict[str, float]:
        """
        Analyze sentiment over time using word timestamps.
        
        Args:
            text: Input text
            timestamps: List of (word, start_time, end_time) tuples
            
        Returns:
            Dictionary mapping timestamps to sentiment scores
        """
        try:
            # Group words by time windows
            time_windows = {}
            window_size = 5  # seconds
            
            for word, start_time, _ in timestamps:
                window = int(start_time / window_size)
                if window not in time_windows:
                    time_windows[window] = []
                time_windows[window].append(word)
            
            # Analyze sentiment for each time window
            sentiment_scores = {}
            for window, words in time_windows.items():
                text_window = ' '.join(words)
                result = self.analyzer(text_window)[0]
                score = 1 if result['label'] == 'POSITIVE' else -1
                score *= result['score']
                sentiment_scores[str(window * window_size)] = score
                
            return sentiment_scores
            
        except Exception as e:
            raise Exception(f"Error analyzing timeline sentiment: {str(e)}")
            
    def get_emotion_scores(self, text: str) -> Dict[str, float]:
        """
        Get emotion scores for the text.
        
        Args:
            text: Input text
            
        Returns:
            Dictionary containing emotion scores
        """
        try:
            # Define basic emotions
            emotions = ['joy', 'sadness', 'anger', 'fear', 'surprise']
            
            # Initialize scores
            emotion_scores = {emotion: 0.0 for emotion in emotions}
            
            # Analyze sentiment
            result = self.analyzer(text)[0]
            
            # Map sentiment to emotions
            if result['label'] == 'POSITIVE':
                emotion_scores['joy'] = result['score']
            else:
                emotion_scores['sadness'] = result['score']
                
            return emotion_scores
            
        except Exception as e:
            raise Exception(f"Error getting emotion scores: {str(e)}")
            
    def analyze_key_points(self, text: str, num_points: int = 5) -> List[Dict]:
        """
        Analyze sentiment of key points in the text.
        
        Args:
            text: Input text
            num_points: Number of key points to analyze
            
        Returns:
            List of dictionaries containing key points and their sentiment
        """
        try:
            # Split text into sentences
            sentences = self._split_into_sentences(text)
            
            # Analyze sentiment for each sentence
            sentence_scores = []
            for sentence in sentences:
                result = self.analyzer(sentence)[0]
                score = 1 if result['label'] == 'POSITIVE' else -1
                score *= result['score']
                sentence_scores.append({
                    'text': sentence,
                    'sentiment': score
                })
            
            # Sort by absolute sentiment score
            sentence_scores.sort(key=lambda x: abs(x['sentiment']), reverse=True)
            
            # Return top N key points
            return sentence_scores[:num_points]
            
        except Exception as e:
            raise Exception(f"Error analyzing key points: {str(e)}") 
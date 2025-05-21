from transformers import pipeline
from typing import List, Dict
import numpy as np

class VideoSummarizer:
    def __init__(self):
        # Initialize the summarization pipeline
        self.summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
        
    def summarize(self, text: str, max_length: int = 150, min_length: int = 30) -> str:
        """
        Generate a summary from the input text.
        
        Args:
            text: Input text to summarize
            max_length: Maximum length of the summary
            min_length: Minimum length of the summary
            
        Returns:
            Generated summary
        """
        try:
            # Split text into chunks if it's too long
            chunks = self._split_text(text)
            
            # Summarize each chunk
            summaries = []
            for chunk in chunks:
                summary = self.summarizer(chunk, 
                                        max_length=max_length,
                                        min_length=min_length,
                                        do_sample=False)
                summaries.append(summary[0]['summary_text'])
            
            # Combine summaries
            final_summary = ' '.join(summaries)
            
            # If the combined summary is too long, summarize it again
            if len(final_summary.split()) > max_length:
                final_summary = self.summarizer(final_summary,
                                             max_length=max_length,
                                             min_length=min_length,
                                             do_sample=False)[0]['summary_text']
            
            return final_summary
            
        except Exception as e:
            raise Exception(f"Error generating summary: {str(e)}")
            
    def _split_text(self, text: str, max_chunk_length: int = 1024) -> List[str]:
        """
        Split text into chunks of maximum length.
        
        Args:
            text: Input text
            max_chunk_length: Maximum length of each chunk
            
        Returns:
            List of text chunks
        """
        words = text.split()
        chunks = []
        current_chunk = []
        current_length = 0
        
        for word in words:
            if current_length + len(word) + 1 <= max_chunk_length:
                current_chunk.append(word)
                current_length += len(word) + 1
            else:
                chunks.append(' '.join(current_chunk))
                current_chunk = [word]
                current_length = len(word)
        
        if current_chunk:
            chunks.append(' '.join(current_chunk))
            
        return chunks
        
    def extract_key_points(self, text: str, num_points: int = 5) -> List[str]:
        """
        Extract key points from the text.
        
        Args:
            text: Input text
            num_points: Number of key points to extract
            
        Returns:
            List of key points
        """
        try:
            # Split text into sentences
            sentences = text.split('. ')
            
            # Generate summary for each sentence
            sentence_scores = []
            for sentence in sentences:
                if len(sentence.split()) > 10:  # Only consider sentences with more than 10 words
                    summary = self.summarizer(sentence,
                                           max_length=50,
                                           min_length=10,
                                           do_sample=False)
                    # Calculate importance score based on summary length
                    score = len(summary[0]['summary_text'].split()) / len(sentence.split())
                    sentence_scores.append((sentence, score))
            
            # Sort sentences by score and get top N
            sentence_scores.sort(key=lambda x: x[1], reverse=True)
            key_points = [s[0] for s in sentence_scores[:num_points]]
            
            return key_points
            
        except Exception as e:
            raise Exception(f"Error extracting key points: {str(e)}")
            
    def generate_timeline(self, text: str, timestamps: List[tuple]) -> Dict[str, str]:
        """
        Generate a timeline of events from the text and timestamps.
        
        Args:
            text: Input text
            timestamps: List of (word, start_time, end_time) tuples
            
        Returns:
            Dictionary mapping timestamps to event descriptions
        """
        try:
            # Extract key points
            key_points = self.extract_key_points(text)
            
            # Match key points with timestamps
            timeline = {}
            for point in key_points:
                # Find the timestamp for the first word in the key point
                first_word = point.split()[0].lower()
                for word, start_time, _ in timestamps:
                    if word.lower() == first_word:
                        timeline[f"{start_time:.2f}"] = point
                        break
            
            return timeline
            
        except Exception as e:
            raise Exception(f"Error generating timeline: {str(e)}") 
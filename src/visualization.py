import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from typing import List, Dict
import os

class Visualizer:
    def __init__(self):
        # Set style for plots
        plt.style.use('seaborn')
        sns.set_palette("husl")
        
    def create_visualizations(self, frames: List[np.ndarray], sentiment: Dict, output_dir: str):
        """
        Create various visualizations for the video analysis.
        
        Args:
            frames: List of video frames
            sentiment: Dictionary containing sentiment analysis results
            output_dir: Directory to save the visualizations
        """
        try:
            # Create output directory if it doesn't exist
            os.makedirs(output_dir, exist_ok=True)
            
            # Generate different types of visualizations
            self._plot_sentiment_timeline(sentiment, output_dir)
            self._plot_frame_analysis(frames, output_dir)
            self._create_summary_visualization(frames, sentiment, output_dir)
            
        except Exception as e:
            raise Exception(f"Error creating visualizations: {str(e)}")
            
    def _plot_sentiment_timeline(self, sentiment: Dict, output_dir: str):
        """
        Create a timeline visualization of sentiment analysis.
        
        Args:
            sentiment: Dictionary containing sentiment analysis results
            output_dir: Directory to save the visualization
        """
        try:
            plt.figure(figsize=(12, 6))
            
            # Extract timestamps and sentiment scores
            timestamps = list(sentiment.keys())
            scores = list(sentiment.values())
            
            # Create the plot
            plt.plot(timestamps, scores, marker='o')
            plt.title('Sentiment Analysis Timeline')
            plt.xlabel('Time (seconds)')
            plt.ylabel('Sentiment Score')
            plt.grid(True)
            
            # Save the plot
            output_path = os.path.join(output_dir, 'sentiment_timeline.png')
            plt.savefig(output_path)
            plt.close()
            
        except Exception as e:
            raise Exception(f"Error plotting sentiment timeline: {str(e)}")
            
    def _plot_frame_analysis(self, frames: List[np.ndarray], output_dir: str):
        """
        Create visualizations for frame analysis.
        
        Args:
            frames: List of video frames
            output_dir: Directory to save the visualization
        """
        try:
            # Calculate frame statistics
            brightness = [np.mean(frame) for frame in frames]
            contrast = [np.std(frame) for frame in frames]
            
            # Create subplots
            fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))
            
            # Plot brightness
            ax1.plot(brightness, label='Brightness')
            ax1.set_title('Frame Brightness Over Time')
            ax1.set_xlabel('Frame Number')
            ax1.set_ylabel('Brightness')
            ax1.grid(True)
            
            # Plot contrast
            ax2.plot(contrast, label='Contrast')
            ax2.set_title('Frame Contrast Over Time')
            ax2.set_xlabel('Frame Number')
            ax2.set_ylabel('Contrast')
            ax2.grid(True)
            
            # Adjust layout and save
            plt.tight_layout()
            output_path = os.path.join(output_dir, 'frame_analysis.png')
            plt.savefig(output_path)
            plt.close()
            
        except Exception as e:
            raise Exception(f"Error plotting frame analysis: {str(e)}")
            
    def _create_summary_visualization(self, frames: List[np.ndarray], sentiment: Dict, output_dir: str):
        """
        Create a comprehensive summary visualization.
        
        Args:
            frames: List of video frames
            sentiment: Dictionary containing sentiment analysis results
            output_dir: Directory to save the visualization
        """
        try:
            # Create a figure with subplots
            fig = plt.figure(figsize=(15, 10))
            
            # Plot 1: Sentiment Distribution
            plt.subplot(2, 2, 1)
            sentiment_scores = list(sentiment.values())
            sns.histplot(sentiment_scores, bins=20)
            plt.title('Sentiment Score Distribution')
            plt.xlabel('Sentiment Score')
            plt.ylabel('Frequency')
            
            # Plot 2: Frame Brightness Distribution
            plt.subplot(2, 2, 2)
            brightness = [np.mean(frame) for frame in frames]
            sns.histplot(brightness, bins=20)
            plt.title('Frame Brightness Distribution')
            plt.xlabel('Brightness')
            plt.ylabel('Frequency')
            
            # Plot 3: Sentiment vs Time
            plt.subplot(2, 2, 3)
            timestamps = list(sentiment.keys())
            plt.plot(timestamps, sentiment_scores)
            plt.title('Sentiment Over Time')
            plt.xlabel('Time (seconds)')
            plt.ylabel('Sentiment Score')
            
            # Plot 4: Frame Statistics
            plt.subplot(2, 2, 4)
            contrast = [np.std(frame) for frame in frames]
            plt.scatter(brightness, contrast, alpha=0.5)
            plt.title('Frame Brightness vs Contrast')
            plt.xlabel('Brightness')
            plt.ylabel('Contrast')
            
            # Adjust layout and save
            plt.tight_layout()
            output_path = os.path.join(output_dir, 'summary_visualization.png')
            plt.savefig(output_path)
            plt.close()
            
        except Exception as e:
            raise Exception(f"Error creating summary visualization: {str(e)}")
            
    def create_heatmap(self, data: np.ndarray, output_dir: str, title: str = 'Heatmap'):
        """
        Create a heatmap visualization.
        
        Args:
            data: 2D numpy array for heatmap
            output_dir: Directory to save the visualization
            title: Title for the heatmap
        """
        try:
            plt.figure(figsize=(10, 8))
            sns.heatmap(data, cmap='YlOrRd', annot=True, fmt='.2f')
            plt.title(title)
            
            output_path = os.path.join(output_dir, f'{title.lower().replace(" ", "_")}.png')
            plt.savefig(output_path)
            plt.close()
            
        except Exception as e:
            raise Exception(f"Error creating heatmap: {str(e)}") 
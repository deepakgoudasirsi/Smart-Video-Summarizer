import cv2
import numpy as np
from typing import List, Tuple
import ffmpeg

class VideoProcessor:
    def __init__(self):
        self.frame_interval = 1  # Extract 1 frame per second
        
    def process_video(self, video_path: str) -> List[np.ndarray]:
        """
        Process video and extract frames at regular intervals.
        
        Args:
            video_path: Path to the video file or URL
            
        Returns:
            List of extracted frames
        """
        try:
            # Get video information
            probe = ffmpeg.probe(video_path)
            video_info = next(s for s in probe['streams'] if s['codec_type'] == 'video')
            fps = eval(video_info['r_frame_rate'])
            
            # Open video
            cap = cv2.VideoCapture(video_path)
            if not cap.isOpened():
                raise ValueError(f"Could not open video: {video_path}")
            
            frames = []
            frame_count = 0
            
            while True:
                ret, frame = cap.read()
                if not ret:
                    break
                    
                # Extract frame at regular intervals
                if frame_count % int(fps * self.frame_interval) == 0:
                    frames.append(frame)
                    
                frame_count += 1
            
            cap.release()
            return frames
            
        except Exception as e:
            raise Exception(f"Error processing video: {str(e)}")
            
    def extract_key_frames(self, frames: List[np.ndarray], threshold: float = 0.5) -> List[np.ndarray]:
        """
        Extract key frames based on significant changes between consecutive frames.
        
        Args:
            frames: List of video frames
            threshold: Threshold for considering a frame as key frame
            
        Returns:
            List of key frames
        """
        key_frames = [frames[0]]
        
        for i in range(1, len(frames)):
            # Calculate difference between consecutive frames
            diff = cv2.absdiff(frames[i], frames[i-1])
            diff_mean = np.mean(diff)
            
            if diff_mean > threshold:
                key_frames.append(frames[i])
                
        return key_frames
        
    def detect_scene_changes(self, frames: List[np.ndarray]) -> List[int]:
        """
        Detect scene changes in the video.
        
        Args:
            frames: List of video frames
            
        Returns:
            List of frame indices where scene changes occur
        """
        scene_changes = []
        prev_hist = None
        
        for i, frame in enumerate(frames):
            # Convert frame to grayscale
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            
            # Calculate histogram
            hist = cv2.calcHist([gray], [0], None, [256], [0, 256])
            hist = cv2.normalize(hist, hist).flatten()
            
            if prev_hist is not None:
                # Calculate histogram difference
                diff = cv2.compareHist(prev_hist, hist, cv2.HISTCMP_CORREL)
                
                if diff < 0.5:  # Threshold for scene change
                    scene_changes.append(i)
                    
            prev_hist = hist
            
        return scene_changes 
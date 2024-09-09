import os
import random
from moviepy.editor import VideoFileClip

# Define the range of durations (in seconds)
MIN_DURATION = 5
MAX_DURATION = 7

# Define the number of clips (GIFs or video chunks) to generate
NUM_CLIPS = 5

# Input video file path and output folder for GIFs or video chunks
video_path = 'videoplayback (3).mp4'
output_folder = 'output_clips/'

# Create output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Load the video
clip = VideoFileClip(video_path)
video_duration = clip.duration  # Get video duration in seconds

# Ask user for the desired output format (GIF or video chunks)
output_format = input("Enter output format ('gif' or 'video'): ").strip().lower()

# Generate random start times and create clips (GIFs or video chunks)
for i in range(NUM_CLIPS):
    # Randomly select the start time of the clip
    start_time = random.uniform(0, video_duration - MAX_DURATION)
    # Randomly choose the duration of the clip between MIN_DURATION and MAX_DURATION
    clip_duration = random.uniform(MIN_DURATION, MAX_DURATION)

    # Create the clip by sub-clipping the video
    subclip = clip.subclip(start_time, start_time + clip_duration)

    # Define the output file path
    if output_format == 'gif':
        clip_filename = f'clip_{i + 1}.gif'
        clip_output_path = os.path.join(output_folder, clip_filename)
        subclip.write_gif(clip_output_path, fps=15)  # Export as GIF
    else:
        # Preserve the same format as the input video (e.g., MP4)
        ext = os.path.splitext(video_path)[1]  # Get the original file extension (e.g., .mp4)
        clip_filename = f'clip_{i + 1}{ext}'
        clip_output_path = os.path.join(output_folder, clip_filename)
        subclip.write_videofile(clip_output_path, codec='libx264')  # Export as video

    print(f"Created clip: {clip_output_path} (Duration: {clip_duration:.2f} seconds)")

# Close the video clip
clip.close()

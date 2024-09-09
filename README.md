# Video to GIF or Video Chunk Converter

This Python script cuts a video into multiple random segments and converts each segment into either a GIF or smaller video chunks, based on user preference. You can customize the number of clips and their durations. Each clip is created with a randomly selected duration between 5 to 7 seconds(which can be modified).

## Requirements

To run this script, you will need to install the following Python package:

```bash
pip install moviepy
```

## How It Works

1. The script loads a video file specified by the user.
2. It then randomly selects segments from the video.
3. Each segment is between 5 to 7 seconds long (which can be modified).
4. The user can choose to save these segments either as GIFs or as smaller video chunks in the original format of the video.
5. The script saves the selected output format in the `output_clips` folder.

## Usage

1. Clone the repository or download the script.
2. Install the required dependencies using `pip`:

   ```bash
   pip install moviepy
   ```

3. Update the script with the path to your video file:

   ```python
   video_path = 'your_video_file.mp4'
   ```

4. Run the script:

   ```bash
   python video_to_clip.py
   ```

5. When prompted, select the output format by typing 'gif' for GIFs or 'video' for smaller video chunks.

6. The clips will be saved in the `output_clips/` folder.

## Parameters

You can adjust the following parameters in the script:

- **MIN_DURATION**: The minimum duration of each clip (default is 5 seconds).
- **MAX_DURATION**: The maximum duration of each clip (default is 7 seconds).
- **NUM_CLIPS**: The number of clips to generate (default is 5).
- **output_format**: Can be set to either 'gif' or 'video'.

## Example

If you input a 5-minute video and set the script to generate 5 clips, the output will be 5 random clips with durations ranging between 5 to 7 seconds, all saved in the `output_clips` folder. The format of the clips depends on your chosen output ('gif' or the original video format).

## Folder Structure

```bash
.
├── video_to_clip.py        # The Python script
├── your_video_file.mp4     # The video you want to convert
└── output_clips/           # Output folder containing generated GIFs or video chunks
```

# Neural Art Generator

This Python script combines a cubic Bézier curve with the Neural Art rendering library to generate a series of artistic images. The script saves these images in the specified output directory. To fully appreciate the creative evolution, it's recommended to compile these images into a video.

## Prerequisites
Python 3
PIL (Python Imaging Library)
NumPy
neuralart (Install via pip install neuralart)

## Usage
1. Clone or download the repository to your local machine.
2. Install the required dependencies:
```bash
pip install Pillow numpy neuralart
```

3. Open a terminal and navigate to the project directory.
4. Run the script with the following command:
```bash
python neural_art_generator.py /path/to/output_directory
```

## Additional Notes
- The script takes one argument: the output directory for saving generated images.
- Ensure the output directory exists; otherwise, it will be created.
- Generated images are saved in the "output_images" subdirectory within the specified output directory.

## Video Creation
To compile the images into a video, use FFmpeg. If FFmpeg is not installed, you can install it using:

```bash
sudo apt-get install ffmpeg   # For Ubuntu
brew install ffmpeg           # For macOS
```

Then, run the following command:
```bash
 ffmpeg -framerate 30 -pattern_type glob -i "output_images/*.png" -i Arnor.mp3 -c:v libx264 -pix_fmt yuv420p -c:a aac -strict experimental -b:a 192k -shortest output_video_with_music.mp4
```

Adjust the input path, output video name.

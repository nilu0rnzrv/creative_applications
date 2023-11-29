Neural Art Generator

This Python script combines a cubic Bézier curve with the Neural Art rendering library to generate a series of artistic images. The script saves these images in the specified output directory. To fully appreciate the creative evolution, it's recommended to compile these images into a video.

Prerequisites
Python 3
PIL (Python Imaging Library)
NumPy
neuralart (Install via pip install neuralart)

Usage
Clone or download the repository to your local machine.

Install the required dependencies:
pip install Pillow numpy neuralart

Open a terminal and navigate to the project directory.
Run the script with the following command:
python neural_art_generator.py /path/to/output_directory

Additional Notes
The script takes one argument: the output directory for saving generated images.

Ensure the output directory exists; otherwise, it will be created.

Generated images are saved in the "output_images" subdirectory within the specified output directory.

Video Creation
To compile the images into a video, use FFmpeg. If FFmpeg is not installed, you can install it using:

sudo apt-get install ffmpeg   # For Ubuntu
brew install ffmpeg           # For macOS

Then, run the following command:
ffmpeg -r 24 -i /path/to/output_directory/image_%04d_iter_%0.2f.png -vf "scale=1024:-1" -pix_fmt yuv420p output_video.mp4

Adjust the input path, output video name.

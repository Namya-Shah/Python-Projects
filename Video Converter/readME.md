# Video Converter

## MP4 to MP3 Converter Readme

This code extracts the audio from an MP4 video file and saves it as an MP3 audio file using the MoviePy library in Python. It allows you to convert the audio track of an MP4 video into a standalone MP3 audio file.

### Prerequisites

- Python 3.x installed on your system
- MoviePy library installed (`pip install moviepy`)

### Getting Started

1. Ensure that you have the necessary prerequisites installed.
2. Download the code and save it to a Python file, e.g., `mp4_to_mp3_converter.py`.
3. Locate the MP4 video file from which you want to extract the audio.
4. Replace the empty string `""` in the `VideoFileClip` function with the file path of your MP4 video file.
5. Run the code using the command `python mp4_to_mp3_converter.py`.

### Usage

1. Upon running the code, it will load the specified MP4 video file.
2. The code will extract the audio track from the video file.
3. The extracted audio will be saved as an MP3 audio file named "new_audio.mp3" in the same directory as the Python script.

### Customization

- Modify the code to specify a different output file name or path by changing the `"new_audio.mp3"` argument in the `write_audiofile` function.
- Adjust the code to process multiple MP4 files or apply additional transformations to the extracted audio.
- Enhance the code with error handling or additional functionality based on your requirements.

### Dependencies

The code relies on the following library:

- `moviepy`: Used for video and audio editing operations.

### Note

- Ensure that you have the necessary rights and permissions to extract audio from the MP4 video file.
- This code provides a basic implementation and may require further enhancements for handling different video formats, error handling, or advanced audio processing.

## MP4 to GIF Converter Readme

This code converts an MP4 video file to a GIF image using the MoviePy library in Python. It allows you to create a GIF animation from a video file.

### Prerequisites

- Python 3.x installed on your system
- MoviePy library installed (`pip install moviepy`)

### Getting Started

1. Ensure that you have the necessary prerequisites installed.
2. Download the code and save it to a Python file, e.g., `mp4_to_gif_converter.py`.
3. Locate the MP4 video file that you want to convert to a GIF.
4. Replace the `"../Downloads/meme.mp4"` string in the `VideoFileClip` function with the file path of your MP4 video file.
5. Run the code using the command `python mp4_to_gif_converter.py`.

### Usage

1. Upon running the code, it will load the specified MP4 video file.
2. The code will convert the video into a GIF image.
3. The resulting GIF file will be saved as "final.gif" in the same directory as the Python script.

### Customization

- Modify the code to specify a different output file name or path by changing the `"final.gif"` argument in the `write_gif` function.
- Adjust the code to process multiple MP4 files or apply additional transformations to the GIF.
- Enhance the code with error handling or additional functionality based on your requirements.

### Dependencies

The code relies on the following library:

- `moviepy`: Used for video editing operations.

### Note

- Ensure that you have the necessary rights and permissions to convert the MP4 video file to a GIF.
- The resulting GIF file may have a larger file size compared to the original video file.
- This code provides a basic implementation and may require further enhancements for handling different video formats, adjusting GIF parameters, error handling, or advanced video processing.

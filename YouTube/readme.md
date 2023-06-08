# YouTube Downloader

This script allows you to download YouTube videos using the PyTube library. Simply provide the YouTube video URL as a command-line argument, and the script will download the video in the highest resolution available.

## Installation

To run this script, you need to have Python installed on your system. Additionally, you need to install the PyTube library. You can install it using the following command:

```
pip install pytube
```

## Usage

1. Open a terminal or command prompt.
2. Run the script `yt-downloader.py` using Python. Pass the YouTube video URL as a command-line argument.

   Example:
   ```
   python youtube_downloader.py [video_url]
   ```

   Replace `[video_url]` with the URL of the YouTube video you want to download.

3. The script will fetch the video details, such as title and views, and display them on the console.
4. It will then proceed to download the video in the highest available resolution.
5. The downloaded video will be saved to the specified directory.

**Note:** Ensure that you have the necessary permissions to write to the specified directory for downloading the video.

## Example

```
python youtube_downloader.py https://www.youtube.com/watch?v=abcdefghijk
```

## Limitations

- This script uses the PyTube library, which relies on the YouTube Data API. Therefore, it may be subject to limitations imposed by YouTube and the API itself.
- Downloading copyrighted content without proper authorization is against YouTube's terms of service and may infringe upon intellectual property rights. Ensure that you have the necessary permissions or the video is available under a suitable license before downloading.

## Acknowledgments

- This script utilizes the PyTube library to interact with the YouTube API and download videos.
- Thank you to the developers of PyTube for providing a convenient way to work with YouTube videos in Python.
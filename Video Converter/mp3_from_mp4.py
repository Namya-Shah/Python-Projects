# Extracting mp3 from mp4 file

import moviepy
import moviepy.editor

# Put your file path in here

video = moviepy.editor.VideoFileClip("")

audio = video.audio

audio.write_audiofile("new_audio.mp3")
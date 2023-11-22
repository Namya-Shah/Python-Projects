from pytube import YouTube
import ffmpeg

def quality_720p():
    return yt.streams.get_by_itag(22) # TO DOWNLOAD IN 720p QUALITY

def quality_144p():
    return yt.streams.get_by_itag(17) # TO DOWNLOAD IN 144p QUALITY

def quality_360p():
    return yt.streams.get_by_itag(18) # TO DOWNLOAD IN 360p QUALITY

def quality_2160p(output_file):
    video = yt.streams.get_by_itag(313) # TO DOWNLOAD IN 2160p QUALITY
    audio = yt.streams.get_by_itag(251) # TO DOWNLOAD AUDIO
    temp_video = video.download(output_path='.', filename="video_temp.mp4")
    temp_audio = audio.download(output_path=".", filename="audio_temp.webm")
    merge_audio_video = ffmpeg.concat(temp_video, temp_audio, v=1, a=1).output(output_file, strict='experimental').run(overwrite_output=True)
    return merge_audio_video(temp_video, temp_audio)
    
url = input("Enter link: ")
yt = YouTube(url)
print(yt.title)
print(yt.author)
print(yt.length)
print(yt.views)

choice = int(input("Enter a number: "))
if choice == 1:
    quality_144p().download()
elif choice == 2:
    quality_360p().download()
elif choice == 3:
    quality_720p().download()
elif choice == 4:
    quality_2160p()
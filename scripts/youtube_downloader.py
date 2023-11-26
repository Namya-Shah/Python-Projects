from pytube import YouTube
import ffmpeg

def quality_720p():
    return yt.streams.get_by_itag(22) # TO DOWNLOAD IN 720p QUALITY

def quality_144p():
    return yt.streams.get_by_itag(17) # TO DOWNLOAD IN 144p QUALITY

def quality_360p():
    return yt.streams.get_by_itag(18) # TO DOWNLOAD IN 360p QUALITY

def mp3():
    return yt.streams.get_by_itag(251) # TO DOWNLOAD IN MP3 FORMAT WITH HIGHEST QUALITY

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
    mp3().download()
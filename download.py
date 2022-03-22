# pip install pytube
import pytube
from pytube.__main__ import YouTube
from pytube.cli import on_progress

link=input("Paste Youtube Link Here: ")
path = input("Where do you want to download? Please paste the path here: ")
print("Downloading...This screen close automatically after the process end. ")
video=YouTube(link,on_progress_callback=on_progress)
stream=video.streams.get_highest_resolution()
stream.download(path)

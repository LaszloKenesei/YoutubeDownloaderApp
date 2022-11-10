from pytube import YouTube
from tkinter import messagebox

'''print("Title:", ytvideo.title)
print("Number of views:", ytvideo.views)
print(f"Length:{ytvideo.length} sec")
print("Uploader:", ytvideo.author)
print(url)'''


def mp4_download(url, directory, resolution):
    try:
        ytvideo = YouTube(url)
    except:
        messagebox.showwarning("Warning", "This YouTube link does not exist!")
    mp4 = ytvideo.streams.filter(resolution=resolution).first()
    mp4.download(output_path=directory, filename=ytvideo.title + '.mp4')

def mp3_download(url, directory):
    try:
        ytvideo = YouTube(url)
    except:
        messagebox.showwarning("Warning", "This YouTube link does not exist!")
    mp3 = ytvideo.streams.get_audio_only()
    mp3.download(output_path=directory, filename=ytvideo.title + '.mp3')
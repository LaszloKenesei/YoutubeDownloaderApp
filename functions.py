from pytube import YouTube

'''print("Title:", ytvideo.title)
print("Number of views:", ytvideo.views)
print(f"Length:{ytvideo.length} sec")
print("Uploader:", ytvideo.author)
print(url)'''

def mp4_download(url, directory):
    ytvideo = YouTube(url)
    mp4 = ytvideo.streams.get_highest_resolution()
    print(mp4)
    mp4.download(output_path=directory, filename=ytvideo.title + '.mp4')


def mp3_download(url, directory):
    ytvideo = YouTube(url)
    mp3 = ytvideo.streams.get_audio_only()
    print(mp3)
    mp3.download(output_path=directory, filename=ytvideo.title + '.mp3')

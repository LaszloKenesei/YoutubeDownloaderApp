'''from pytube import YouTube

url = input("Please enter the video's link you would like to download: ")
ytvideo = YouTube(url)
print("Title:", ytvideo.title)
print("Number of views:", ytvideo.views)
print(f"Length:{ytvideo.length} sec")
print("Uploader:", ytvideo.author)

def mp4_download():
    #print(ytvideo.streams)
    #print(ytvideo.streams.filter(only_video=True))
    #print(ytvideo.streams.filter(progressive=True))
    mp4 = ytvideo.streams.get_highest_resolution()
    print(mp4)
    mp4.download(output_path="C:/Users/laca4/Downloads/", filename=ytvideo.title + '.mp4')


def mp3_download():
    mp3 = ytvideo.streams.get_audio_only()
    print(mp3)
    mp3.download(output_path="C:/Users/laca4/Downloads/", filename=ytvideo.title + '.mp3')'''
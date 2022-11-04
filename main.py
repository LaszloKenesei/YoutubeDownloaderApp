from pytube import YouTube

url = input("Please enter the video's link you would like to download: ")
ytvideo = YouTube(url)
print("Title:", ytvideo.title)
print("Number of views:", ytvideo.views)
print(f"Length:{ytvideo.length} sec")
print("Uploader:", ytvideo.author)

selection = input("Please select the format you would like to download (mp3/mp4) ")

def mp4_download():
    #print(ytvideo.streams)
    #print(ytvideo.streams.filter(only_video=True))
    #print(ytvideo.streams.filter(progressive=True))
    mp4 = ytvideo.streams.get_highest_resolution()
    print(mp4)
    mp4.download(r"C:\Users\laca4\Downloads")


def mp3_download():
    print(ytvideo.streams)
    mp3 = ytvideo.streams.get_audio_only()
    print(mp3)
    mp3.download(r"C:\Users\laca4\Downloads", )

if selection == "mp4":
    mp4_download()
elif selection == "mp3":
    mp3_download()
else:
    print("Unable to download in this file format! :(")






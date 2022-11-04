import functions
from tkinter import *
root = Tk()

root.geometry('600x400')
root.title('YouTube downloader')
#Label(root, text="Paste the video link below", font=25).place(x=15, y=15)
Button(root,width=20, height=32, borderwidth=1,text="♬ Audio").place(x=200, y=60)
Button(root, text="▶ Video", bd=1).place(x=400, y=60)
Text(root).place (x=300, y=100)

root.mainloop()
'''import tkinter as tk

root = tk.Tk()
root.title("YouTube downloader")
canvas = tk.Canvas(root, width=800, height=400)
canvas.grid(columnspan=3, rowspan=3)
lbl1 = tk.Label(root, text="Paste the video link below", font=25)
lbl1.grid(column=0, row=0)
lbl2 = tk.Label(root, text="Paste the video link below", font=25)
lbl2.grid(column=1, row=0)
mp3bttn = tk.Button(root, text="♬ Audio")
mp3bttn.grid(column=0, row=1)
mp4bttn = tk.Button(root, text="▶ Video")
mp4bttn.grid(column=1, row=1)



root.mainloop()'''
























'''selection = input("Please select the format you would like to download (mp3/mp4) ")

if selection == "mp4":
    functions.mp4_download()
elif selection == "mp3":
    functions.mp4_download()
else:
    print("Unable to download in this file format! :(")'''






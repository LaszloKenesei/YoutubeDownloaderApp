import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
#from functions import mp4_download, mp3_download

audio = None
url = None
def audioBttn_clicked():
    global audio
    resolution['state'] = DISABLED
    resolution.set('')
    audio = True

def videoBttn_clicked():
    global audio
    resolution['state'] = ACTIVE
    audio = False

def downloadBttn_clicked():
    global audio
    global url
    directory = filedialog.askdirectory()
    url = urlEntry.get()
    if audio:
        mp3_download()
    else:
        mp4_download()


root = tk.Tk()

root.geometry('1000x400')
canvas = Canvas(root, width=1000, height=400, bg='white')
canvas.pack()
root.title('YouTube downloader')
canvas.create_rectangle(0, 0, 1000, 70, fill='#e6e6e6', outline="#cccccc")
audioBttn = Button(root, borderwidth=0, text="♬  Audio", font=('Calibri_Light 18'), bg='#e6e6e6', fg='#333333', command=audioBttn_clicked)
audioBttn.place(x=360, y=3, width=140, height=65)

videoBttn = tk.Button(root, borderwidth=0, text="▶  Video", font=('Calibri_Light 18'), bg='#e6e6e6', fg='#333333', command=videoBttn_clicked)
videoBttn.place(x=500, y=3, width=140, height=65)

urlLbl = Label(root, text='URL', anchor="e", fg='#404040', bg='white', justify='left', font=22)
urlLbl.place(x=40, y=120, width=100)

resLbl = Label(root, text='Resolution', anchor="e", fg='#404040', bg='white', justify=RIGHT, font=22)
resLbl.place(x=40, y=175, width=100)

urlEntry = Entry(root, borderwidth=0, bg='#e6e6e6', font=22, justify=CENTER,  selectbackground="red")
urlEntry.place(x=150, y=120,  height=36, width=810)

downloadBttn = Button(root, text='Download', bg='#ff1a1a', fg='#ffffff', justify=CENTER, font=('Calibri_Light 16'), bd=0, command=downloadBttn_clicked)
downloadBttn.place(x=450, y=230, height=35, width=120)

resolution = ttk.Combobox(root, values=['144p', '240p', '360p', '480p', '720p'], state='readonly', font=12)
resolution.place(x=150, y=175, height=36, width=810)
root.option_add('*TCombobox*Listbox.selectBackground', 'red')
root.option_add('*TCombobox*Listbox.selectForeground', 'white')

logo = ImageTk.PhotoImage(Image.open('YouTube_full-color_icon_(2017).jpg').resize((70,50), Image.LANCZOS))
label = Label(root, image=logo)
label.place(x=10, y=10, height=50, width=70)


root.mainloop()

























'''selection = input("Please select the format you would like to download (mp3/mp4) ")

if selection == "mp4":
    functions.mp4_download()
elif selection == "mp3":
    functions.mp4_download()
else:
    print("Unable to download in this file format! :(")'''






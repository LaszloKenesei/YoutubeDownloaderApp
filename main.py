import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
from tkinter import messagebox
from functions import mp3_download, mp4_download

audio = True

def audioBttn_clicked():
    global audio
    selectres['state'] = DISABLED
    selectres.set('')
    audio = True
    audioBttn['bg'] = '#cccccc'
    videoBttn['bg'] = '#e6e6e6'

def videoBttn_clicked():
    global audio
    selectres['state'] = 'readonly'
    audio = False
    videoBttn['bg'] = '#cccccc'
    audioBttn['bg'] = '#e6e6e6'

def downloadBttn_clicked():
    global audio
    url = urlEntry.get()
    resolution = selectres.get()
    if audio:
        directory = filedialog.askdirectory()
        mp3_download(url, directory)
        urlEntry.delete(0, END)
    else:
        if resolution == '':
            messagebox.showwarning("Warning", "Resolution not selected!")
        else:
            directory = filedialog.askdirectory()
            mp4_download(url, directory, resolution)
            urlEntry.delete(0, END)
            selectres.set('')

def on_enter(e):
    if e.widget['bg'] != '#cccccc':
        e.widget['bg'] = '#d9d9d9'

def on_leave(e):
    if e.widget['bg'] != '#cccccc':
        e.widget['bg'] = '#e6e6e6'

def download_enter(e):
    downloadBttn['bg'] = '#ffffff'
    downloadBttn['fg'] = '#ff1a1a'
def download_leave(e):
    downloadBttn['bg'] = '#ff1a1a'
    downloadBttn['fg'] = '#ffffff'

root = tk.Tk()

root.geometry('1000x400')
canvas = Canvas(root, width=1000, height=400, bg='white')
canvas.pack()
root.title('YouTube downloader')
canvas.create_rectangle(0, 0, 1000, 70, fill='#e6e6e6', outline="#cccccc")
audioBttn = Button(root, borderwidth=0, text="♬  Audio", font=('Calibri_Light 18'), bg='#cccccc', fg='#333333', command=audioBttn_clicked)
audioBttn.place(x=360, y=3, width=140, height=65)
audioBttn.bind("<Enter>", on_enter)
audioBttn.bind("<Leave>", on_leave)


videoBttn = tk.Button(root, borderwidth=0, text="▶  Video", font=('Calibri_Light 18'), bg='#e6e6e6', fg='#333333', command=videoBttn_clicked)
videoBttn.place(x=500, y=3, width=140, height=65)
videoBttn.bind("<Enter>", on_enter)
videoBttn.bind("<Leave>", on_leave)

urlLbl = Label(root, text='URL', anchor="e", fg='#404040', bg='white', justify='left', font=22)
urlLbl.place(x=40, y=120, width=100)

resLbl = Label(root, text='Resolution', anchor="e", fg='#404040', bg='white', justify=RIGHT, font=22)
resLbl.place(x=40, y=175, width=100)

urlEntry = Entry(root, borderwidth=0, bg='#e6e6e6', font=22, justify=CENTER,  selectbackground="red")
urlEntry.place(x=150, y=120,  height=36, width=810)

downloadBttn = Button(root, text='Download', bg='#ff1a1a', fg='#ffffff', justify=CENTER, font=('Calibri_Light 16'), bd=0, command=downloadBttn_clicked)
downloadBttn.place(x=450, y=230, height=35, width=120)
downloadBttn.bind("<Enter>", download_enter)
downloadBttn.bind("<Leave>", download_leave)

selectres = ttk.Combobox(root, values=['144p', '240p', '360p', '480p', '720p'], state='disabled', font=12)
selectres.place(x=150, y=175, height=36, width=810)
root.option_add('*TCombobox*Listbox.selectBackground', 'red')
root.option_add('*TCombobox*Listbox.selectForeground', 'white')
root.option_add('*TCombobox*Listbox.fieldBackground', 'white')
selectres.bind("<<ComboboxSelected>>",lambda e: root.focus())

logo = ImageTk.PhotoImage(Image.open('YouTube_full-color_icon_(2017).jpg').resize((70,50), Image.Resampling.LANCZOS))
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






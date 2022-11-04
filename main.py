import functions
from tkinter import *
root = Tk()

root.geometry('700x400')
canvas = Canvas(root, width=700, height=400, bg='white')
canvas.pack()
root.title('YouTube downloader')
Button(root, borderwidth=0, text="♬  Audio", font=('Calibri_Light'), bg='#e6e6e6', fg='#333333').place(x=250, y=3, width=100, height=65)
Button(root, borderwidth=0, text="▶  Video", font=('Calibri_Light'), bg='#e6e6e6', fg='#333333').place(x=350, y=3, width=100, height=65)
Label(root, text='URL', anchor="e", fg='#404040', bg='white', justify='left', font=22).place(x=40, y=170, width=100)
Label(root, text='Resolution', anchor="e", fg='#404040', bg='white', justify=RIGHT, font=22).place(x=40, y=225, width=100)
Text(root, border=1).place (x=150, y=170,  height=36, width=460)
Text(root, border=1).place (x=150, y=225, height=36, width=460)
canvas.create_rectangle(0, 0, 700, 70, fill='#e6e6e6', outline="#cccccc")

root.mainloop()

























'''selection = input("Please select the format you would like to download (mp3/mp4) ")

if selection == "mp4":
    functions.mp4_download()
elif selection == "mp3":
    functions.mp4_download()
else:
    print("Unable to download in this file format! :(")'''






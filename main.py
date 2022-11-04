import functions
from tkinter import *
root = Tk()

root.geometry('1000x400')
canvas = Canvas(root, width=1000, height=400, bg='white')
canvas.pack()
root.title('YouTube downloader')
Button(root, borderwidth=0, text="♬  Audio", font=('Calibri_Light 18'), bg='#e6e6e6', fg='#333333').place(x=360, y=3, width=140, height=65)
Button(root, borderwidth=0, text="▶  Video", font=('Calibri_Light 18'), bg='#e6e6e6', fg='#333333').place(x=500, y=3, width=140, height=65)
Label(root, text='URL', anchor="e", fg='#404040', bg='white', justify='left', font=22).place(x=40, y=120, width=100)
Label(root, text='Resolution', anchor="e", fg='#404040', bg='white', justify=RIGHT, font=22).place(x=40, y=175, width=100)
Entry(root, borderwidth=0, bg='#e6e6e6', font=22, justify=CENTER, selectbackground="red").place(x=150, y=120,  height=36, width=810)
Combobox(root, borderwidth=0, bg='#e6e6e6', font=10, justify=CENTER, selectbackground="red").place(x=150, y=175, height=36, width=810)
Button(root, text='Download', bg='#ff1a1a', fg='#ffffff', justify=CENTER, font=('Calibri_Light 16'), bd=0).place(x=450, y=230, height=35, width=120)
canvas.create_rectangle(0, 0, 1000, 70, fill='#e6e6e6', outline="#cccccc")

root.mainloop()

























'''selection = input("Please select the format you would like to download (mp3/mp4) ")

if selection == "mp4":
    functions.mp4_download()
elif selection == "mp3":
    functions.mp4_download()
else:
    print("Unable to download in this file format! :(")'''






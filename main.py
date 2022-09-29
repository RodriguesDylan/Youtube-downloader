from tkinter import ttk
from pytube import YouTube
from tkinter import *
from tkinter import ttk


# yt = YouTube('https://www.youtube.com/watch?v=mC5s9KcaHHY')

# print(yt.streams.filter(file_extension='mp4'))

# stream = yt.streams.get_audio_only()
# stream.download()

root = Tk()

root.title("Youtube-downloader")

mainframe = ttk.Frame(root, padding='3 3 12 12', width=300, height=200)
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

root.mainloop()

import tkinter
import customtkinter
from pytube import YouTube


def startDownload():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink)
        video = ytObject.streams.get_highest_resolution()
        video.download()
    except:
        finishLabel.configure(text='Download error')
    finishLabel.configure(text='Download Complete')


# System settings
customtkinter.set_appearance_mode('System')
customtkinter.set_default_color_theme('blue')

# App frame
app = customtkinter.CTk()
app.geometry('720x480')
app.title('YouTube Video Downloader')

# Add UI elements
title = customtkinter.CTkLabel(app, text='Insert a YouTube link')
title.pack(padx=10, pady=10)

# Link input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

# Finished downloading
finishLabel = customtkinter.CTkLabel(app, text='')
finishLabel.pack()

# Download button
download = customtkinter.CTkButton(app, text='Download', command=startDownload)
download.pack(padx=10, pady=10)

# Run app
app.mainloop()

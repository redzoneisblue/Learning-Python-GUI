import tkinter
import customtkinter
from pytube import YouTube

def startDownload():
    try: 
        ytlink = link.get()
        ytObject = YouTube(ytlink)
        video = ytObject.streams.get_highest_resolution()
        video.download()
        print("Download complete.")
    except:
        print("Youtube link is invalid")
    


#System Settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

#Our app frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("YouTube Downloader")

#Adding UI Elements
title = customtkinter.CTkLabel(app, text="Insert a YouTube link")
title.pack(padx=10, pady=10)

#Link Input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40)
link.pack()

#Download button
download = customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack(padx=20,pady=20)

#Run app
app.mainloop()
import tkinter
import customtkinter
from pytube import YouTube

def startDownload():
    try: 
        ytlink = link.get()
        ytObject = YouTube(ytlink)
        video = ytObject.streams.get_highest_resolution()
        video.download()
        status_label.configure(text="Download complete.")
    except Exception as e:
        status_label.configure(text=f"Error: {str(e)}")
    


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
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

#Download button
download = customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack(padx=20,pady=20)

# Status label
status_label = customtkinter.CTkLabel(app, text="")
status_label.pack(padx=10, pady=10)

#Run app
app.mainloop()
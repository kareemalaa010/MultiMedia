from tkinter import *
from yt_dlp import YoutubeDL

# function download the videos with high Qualtiy
def high_quality():
    try:
        link = entry.get()
        
        ydl_opts = {
            'format' : 'best',
            'outtmpl' : 'downloads%(titles)s.%(ext)s'
        }

        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])

            print("downlaod video successfully !")

    except Exception as e :
        print("Error with downloading")

# function download the videos with low Qualtiy
def low_quality():
    try:
        link = entry.get()
        
        ydl_opts = {
            'format' : 'warest',
            'outtmpl' : 'downloads%(titles)s.%(ext)s'
        }

        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])

            print("downlaod video successfully !")

    except Exception as e :
        print("Error with downloading")

# function is get audio
def get_audio():
    try:
        link = entry.get()
        
        ydl_opts = {
            'format' : 'bestaudio',
            'outtmpl' : 'downloads%(titles)s.%(ext)s'
        }

        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])

            print("downlaod video successfully !")

    except Exception as e :
        print("Error with downloading")


# frame with TKinter libaray
myframe = Tk()
myframe.title("layout")
myframe.geometry("600x400")
myframe.config(bg = "#EEDFCC")

# label with the frame
label = Label(myframe , text = "add your link" , font = "bold" , bg = myframe['bg'])
label.place(x = 250 , y = 30)

# field input i will enter the link in it
entry = Entry(myframe , width = 55)
entry.place(x = 110  , y = 100)

# button download with high
high = Button(myframe , text = "High Qualtiy" , command = high_quality , font="bold" , activebackground="green")
high.place(x= 100 , y = 200)

# button download with low
low = Button(myframe , text = "Low Qualtiy" , command = low_quality , font="bold" , activebackground="red")
low.place(x= 250 , y = 200)

# button download with audio
audio = Button(myframe , text = "Get Audio" , command = get_audio , font="bold" , activebackground="blue")
audio.place(x= 400 , y = 200)

# loop the frame 
myframe.mainloop()
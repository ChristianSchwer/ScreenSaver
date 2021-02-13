from tkinter import *
from tkinter.ttk import *
from time import *
from datetime import *
from PIL import Image
from PIL import ImageTk

class Fullscreen:
    def __init__(self):
        self.window = Tk()
        self.window.attributes('-fullscreen', True)
        self.fullScreenState = False
        self.window.bind("<Escape>",self.quitFullScreen)
        self.window.bind("<Button-1>", self.quitFullScreen)
        self.window.bind("<Button-2>", self.quitFullScreen)
        self.window.bind("<Button-3>", self.quitFullScreen)
        self.window.bind("<Motion>", self.quitFullScreen)

        #Get screen resolutions
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

        #Add image file
        #filename = "D:\Privat\Bilder\Lonely-Boat-Dragon-Bones-LIve-Wallpaper.gif"
        filename = "D:\Privat\Bilder\IMG_3750.JPG"
        background_image = Image.open(filename)
        background_image = background_image.resize((screen_width, screen_height), Image.ANTIALIAS)
        background_image = ImageTk.PhotoImage(background_image)

        #Create Canvas
        canvas = Canvas(self.window, width = 1020, height = 1080)
        canvas.pack(fill = "both", expand = True)

        canvas.create_image(0, 0, image = background_image, anchor = "nw")
        timerObj = canvas.create_text((screen_width/2, screen_height/2), font = ('calibri', 30, 'bold'), fill = 'white', text = '')
        timeObj = canvas.create_text((screen_width/2, screen_height/4), font = ('calibri', 30, 'bold'), fill = 'white', text = '')

        end_Date = datetime(year=2025, month=1, day=1, hour=0, minute=0, second=0)

        Countdown(canvas, end_Date, timerObj)
        time(canvas, timeObj)
        self.window.mainloop()

    def quitFullScreen(self, event):
        self.fullScreenState = False   #   only minimize
        self.window.attributes("-fullscreen", self.fullScreenState)    #   only minimize
        #self.window.destroy()      #-  close window

def Countdown(canvas, end_Date, timerObj):
    now = datetime.now()
    years = end_Date.year - now.year - ((end_Date.month, end_Date.day) < (now.month, now.day))
    months =  11 - (now.month - end_Date.month)
    days = 27 - (now.day - end_Date.day)
    hours = 23 - now.hour - end_Date.hour
    minutes = 59 - now.minute - end_Date.minute
    seconds = 60 - now.second - end_Date.second
    text = 'Years ' + str(years) + '    Months ' + str(months) + '    Days ' + str(days) +\
        '    Hours ' + str(hours) + '    Minutes ' + str(minutes) + '    Seconds ' + str(seconds)
    if int(end_Date.strftime('%Y%m%d%H%M%S')) > 0:
        canvas.itemconfigure(timerObj, text = text)
        canvas.after(1000, Countdown, canvas, end_Date, timerObj)

def time(canvas, timeObj):
    string = strftime('%H:%M:%S')
    canvas.itemconfigure(timeObj, text = string)
    canvas.after(1000, time, canvas, timeObj)

if __name__ == '__main__':
    app = Fullscreen()

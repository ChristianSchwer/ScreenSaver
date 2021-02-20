from tkinter import *
from tkinter.ttk import *
from time import *
from datetime import *
from PIL import Image, ImageTk
import keyboard
import mouse

last_input = datetime.now()
lastPosition = mouse.get_position()

class Fullscreen:
    def __init__(self):
        self.window = Tk()
        self.window.attributes('-fullscreen', True)
        self.fullScreenState = False
        UserInput(self)

        #Get screen resolutions
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

        #Add image file
        filename = "D:\Privat\Bilder\IMG_3750.JPG"
        background_image = Image.open(filename)
        background_image = background_image.resize((screen_width, screen_height), Image.ANTIALIAS)
        background_image = ImageTk.PhotoImage(background_image)

        #Add gif file
        gif_filename = 'D:\\Privat\\Bilder\\Lonely-Boat-Dragon-Bones-LIve-Wallpaper.gif' #'D:\\Privat\\Bilder\\animated-wallpaper-windows-10.gif'
        gif = Image.open(gif_filename)
        #Add and count frames
        frames = []
        try:
            while 1:
                gif1 = gif.resize((screen_width, screen_height), Image.ANTIALIAS)
                frames.append(ImageTk.PhotoImage(gif1.copy()))
                gif.seek(len(frames))
        except EOFError:
            pass
        frameCnt = len(frames)

        #Create Canvas
        canvas = Canvas(self.window, width = 1020, height = 1080)
        canvas.pack(fill = "both", expand = True)

        #Create picture and text on canvas
        canvas.create_image(0, 0, image = background_image, anchor = "nw")
        animationObj = canvas.create_image(0, 0, image = frames[0], anchor = "nw")
        timerObj = canvas.create_text((screen_width/2, screen_height/2), font = ('calibri', 30, 'bold'), fill = 'white', text = '')
        timeObj = canvas.create_text((screen_width/2, screen_height/4), font = ('calibri', 30, 'bold'), fill = 'white', text = '')

        #End date for the timer
        end_Date = datetime(year=2025, month=1, day=1, hour=0, minute=0, second=0)

        Update(canvas, 0, animationObj, frames, frameCnt)
        Countdown(canvas, end_Date, timerObj)
        Time(canvas, timeObj)

        self.window.mainloop()

def QuitFullScreen(self):
    self.fullScreenState = False   #   only minimize
    self.window.attributes("-fullscreen", self.fullScreenState)    #   only minimize
    global last_input
    last_input = datetime.now()
    FullScreen(self)

def UserInput(self):
    global lastPosition
    currentPosition = mouse.get_position()
    if (keyboard.is_pressed("space") or keyboard.is_pressed("enter") or keyboard.is_pressed("q")
     or keyboard.is_pressed("w") or keyboard.is_pressed("e") or keyboard.is_pressed("r")
     or keyboard.is_pressed("t") or keyboard.is_pressed("z") or keyboard.is_pressed("u")
     or keyboard.is_pressed("i") or keyboard.is_pressed("o") or keyboard.is_pressed("p")
     or keyboard.is_pressed("a") or keyboard.is_pressed("s") or keyboard.is_pressed("d")
     or keyboard.is_pressed("f") or keyboard.is_pressed("g") or keyboard.is_pressed("h")
     or keyboard.is_pressed("j") or keyboard.is_pressed("k") or keyboard.is_pressed("l")
     or keyboard.is_pressed("y") or keyboard.is_pressed("x") or keyboard.is_pressed("c")
     or keyboard.is_pressed("v") or keyboard.is_pressed("b") or keyboard.is_pressed("n")
     or keyboard.is_pressed("m") or keyboard.is_pressed("ü") or keyboard.is_pressed("ä")
     or keyboard.is_pressed("ö") or keyboard.is_pressed(",") or keyboard.is_pressed(".")
     or keyboard.is_pressed("-") or keyboard.is_pressed("#") or keyboard.is_pressed("+")):
        QuitFullScreen(self)
    if (mouse.is_pressed("right")):
        QuitFullScreen(self)
    if (mouse.is_pressed("middle")):
        QuitFullScreen(self)
    if (mouse.is_pressed("left")):
        QuitFullScreen(self)
    if (currentPosition != lastPosition):
        lastPosition = mouse.get_position()
        QuitFullScreen(self)
    self.window.after(100, UserInput, self)

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

def Time(canvas, timeObj):
    string = strftime('%H:%M:%S')
    canvas.itemconfigure(timeObj, text = string)
    canvas.after(1000, Time, canvas, timeObj)

def Update(canvas, ind, gif, frames, frameCnt):
    frame = frames[ind]
    ind += 1
    if ind == frameCnt:
        ind = 0
    canvas.itemconfigure(gif, image=frame)
    canvas.after(100, Update, canvas, ind, gif, frames, frameCnt)

def FullScreen(self):
    current_time = datetime.now()
    inactivityTime = current_time - last_input
    if (inactivityTime.seconds > 5):
        self.fullScreenState = True  # Just toggling the boolean
        self.window.attributes("-fullscreen", self.fullScreenState)
    self.window.after(1000, FullScreen, self)

if __name__ == '__main__':
    app = Fullscreen()

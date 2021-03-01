from tkinter import *
from tkinter.ttk import *
from time import *
from datetime import *
from PIL import Image, ImageTk
import keyboard
import mouse
#from Xlib import X, display
#from Xlib.ext import randr

last_input = datetime.now()
lastPosition = mouse.get_position()

class GUI:
    def __init__(self):
        gui = Tk()
        gui.geometry("600x400")

        #GUI enteries
        canvasG = Canvas(gui, width = 600, height = 400)
        canvasG.pack(fill = "both", expand = True)

        #Enable picture
        enableP = IntVar()
        CheckP = Checkbutton(gui, text='Picture',variable=enableP, onvalue=1, offvalue=0)
        canvasG.create_window(50, 25, window = CheckP)

        labelP = Label(gui, text='Enter picture filename')
        labelP.config(font=('helvetica', 14))
        canvasG.create_window(300, 25, window = labelP)

        picturefile = Entry(gui)
        canvasG.create_window(300, 50, window = picturefile)

        #Enable animation
        enableA = IntVar()
        CheckA = Checkbutton(gui, text='Animation',variable=enableA, onvalue=1, offvalue=0)
        canvasG.create_window(50, 100, window = CheckA)

        labelA = Label(gui, text='Enter animation filename')
        labelA.config(font=('helvetica', 14))
        canvasG.create_window(300, 100, window = labelA)

        animationfile = Entry(gui)
        canvasG.create_window(300, 125, window = animationfile)

        #Enable Time
        enableT = IntVar()
        CheckT = Checkbutton(gui, text='Time',variable=enableT, onvalue=1, offvalue=0)
        canvasG.create_window(50, 175, window = CheckT)

        #Enable Countdown
        enableC = IntVar()
        CheckC = Checkbutton(gui, text='Countdown',variable=enableC, onvalue=1, offvalue=0)
        canvasG.create_window(50, 225, window = CheckC)

        labelD = Label(gui, text='Enter end date YYYY-MM-DD HH:MM:SS')
        labelD.config(font=('helvetica', 14))
        canvasG.create_window(300, 225, window = labelD)

        endDateEntry = Entry(gui)
        canvasG.create_window(300, 250, window = endDateEntry)

        def CreateScreenSaver():
            scs = Toplevel(gui)
            scs.attributes('-fullscreen',True)

            #Get screen resolutions
            screen_width = scs.winfo_screenwidth()
            screen_height = scs.winfo_screenheight()

            #Create Canvas
            canvas = Canvas(scs, width = 1020, height = 1080)
            canvas.pack(fill = "both", expand = True)

            picturefilename = picturefile.get()
            animationfilename = animationfile.get()
            #End date for the timer
            endDate = endDateEntry.get()
            if (endDate == ""):
                end_Date = datetime(year=2025, month=1, day=1, hour=0, minute=0, second=0)
            else:
                end_Date = datetime.strptime(endDate, '%Y-%m-%d %H:%M:%S')

            if (enableP.get() == 1):
                if (picturefilename != ""):
                    #Add image file
                    filename = picturefilename
                    background_image = Image.open(filename)
                    background_image = background_image.resize((screen_width, screen_height), Image.ANTIALIAS)
                    background_image = ImageTk.PhotoImage(background_image)
                    canvas.create_image(0, 0, image = background_image, anchor = "nw")
                else:
                    #Add image file
                    filename = "D:\Privat\Bilder\IMG_3750.JPG"
                    background_image = Image.open(filename)
                    background_image = background_image.resize((screen_width, screen_height), Image.ANTIALIAS)
                    background_image = ImageTk.PhotoImage(background_image)
                    canvas.create_image(0, 0, image = background_image, anchor = "nw")

            if (enableA.get() == 1):
                if (animationfilename != ""):
                    #Add gif file
                    gif_filename = animationfilename
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
                    animationObj = canvas.create_image(0, 0, image = frames[0], anchor = "nw")
                    Animation(canvas, 0, animationObj, frames, frameCnt)
                else:
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
                    animationObj = canvas.create_image(0, 0, image = frames[0], anchor = "nw")
                    Animation(canvas, 0, animationObj, frames, frameCnt)

            UserInput(scs)

            if (enableC.get() == 1):
                timerObj = canvas.create_text((screen_width/2, screen_height/2), font = ('calibri', 30, 'bold'), fill = 'white', text = '')
                Countdown(canvas, end_Date, timerObj)
            if (enableT.get() == 1):
                timeObj = canvas.create_text((screen_width/2, screen_height/4), font = ('calibri', 30, 'bold'), fill = 'white', text = '')
                Time(canvas, timeObj)

            scs.mainloop()

        activateScreenSaver = Button(gui, text="erstellen", command = CreateScreenSaver)
        canvasG.create_window(300, 380, window=activateScreenSaver)
        gui.mainloop()

def QuitFullScreen(scs):
    scs.withdraw()
    global last_input
    last_input = datetime.now()
    FullScreen(scs)

def UserInput(scs):
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
        QuitFullScreen(scs)
    if (mouse.is_pressed("right")):
        QuitFullScreen(scs)
    if (mouse.is_pressed("middle")):
        QuitFullScreen(scs)
    if (mouse.is_pressed("left")):
        QuitFullScreen(scs)
    if (currentPosition != lastPosition):
        lastPosition = mouse.get_position()
        QuitFullScreen(scs)
    scs.after(100, UserInput, scs)

def Countdown(canvas, end_Date, timerObj):
    now = datetime.now()
    years = end_Date.year - now.year - ((end_Date.month, end_Date.day) < (now.month, now.day))
    months =  11 - (now.month - end_Date.month)
    days = 30 - (now.day - end_Date.day)
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

def Animation(canvas, ind, gif, frames, frameCnt):
    frame = frames[ind]
    ind += 1
    if ind == frameCnt:
        ind = 0
    canvas.itemconfigure(gif, image=frame)
    canvas.after(100, Animation, canvas, ind, gif, frames, frameCnt)

def FullScreen(scs):
    current_time = datetime.now()
    inactivityTime = current_time - last_input
    if (inactivityTime.seconds > 5):
        scs.deiconify()
    scs.after(1000, FullScreen, scs)

if __name__ == '__main__':
    app = GUI()

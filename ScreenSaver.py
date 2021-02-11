from tkinter import *
from tkinter.ttk import *
from time import *
from datetime import *

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

        timer_lbl = Label(self.window, font = ('calibri', 30, 'bold'), foreground = 'black')
        time_lbl = Label(self.window, font = ('calibri', 40, 'bold'), foreground = 'black')

        timer_lbl.place(relx = 0.5, rely = 0.5, anchor = 'center')
        time_lbl.place(relx = 0.5, rely = 0.1, anchor = 'center')

        end_Date = datetime(year=2025, month=1, day=1, hour=0, minute=0, second=0)

        Countdown(timer_lbl, end_Date)
        time(time_lbl)

        self.window.mainloop()

    def quitFullScreen(self, event):
        self.fullScreenState = False   #   only minimize
        self.window.attributes("-fullscreen", self.fullScreenState)    #   only minimize
        #self.window.destroy()      #-  close window

def Countdown(lbl1, end_Date):
    now = datetime.now()
    years = end_Date.year - now.year - ((end_Date.month, end_Date.day) < (now.month, now.day))
    months =  11 - (now.month - end_Date.month)
    days = 27 - (now.day - end_Date.day)
    hours = 23 - now.hour - end_Date.hour
    minutes = 59 - now.minute - end_Date.minute
    seconds = 60 - now.second - end_Date.second
    if int(end_Date.strftime('%Y%m%d%H%M%S')) > 0:
        lbl1.config(text = 'Years ' + str(years) +
        '    Months ' + str(months) + '    Days ' + str(days) +
        '    Hours ' + str(hours) + '    Minutes ' + str(minutes) +
        '    Seconds ' + str(seconds))
        lbl1.after(1000, Countdown, lbl1, end_Date)

def time(lbl):
    string = strftime('%H:%M:%S')
    lbl.config(text = string)
    lbl.after(1000, time, lbl)

if __name__ == '__main__':
    app = Fullscreen()

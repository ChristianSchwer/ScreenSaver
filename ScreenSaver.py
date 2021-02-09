import tkinter

class Fullscreen:
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.attributes('-fullscreen', True)
        #self.fullScreenState = False
        self.window.bind("<Escape>",self.quitFullScreen)
        self.window.bind("<Button-1>", self.quitFullScreen)
        self.window.bind("<Button-2>", self.quitFullScreen)
        self.window.bind("<Button-3>", self.quitFullScreen)
        self.window.bind("<Motion>", self.quitFullScreen)

        self.window.mainloop()

    def quitFullScreen(self, event):
        #self.fullScreenState = False   -   only minimize
        #self.window.attributes("-fullscreen", self.fullScreenState)    -   only minimize
        self.window.destroy()

if __name__ == '__main__':
    app = Fullscreen()

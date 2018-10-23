# Import modules
import tkinter


class App(tkinter.Tk):
    def __init__(self):
        #self.title("Sleep Calculator")
        #self.geometry("640x360")
        tkinter.Tk.__init__(self)
        self.label = tkinter.Label(self, text="How many years old are you?")
        self.entry = tkinter.Entry(self)
        self.button = tkinter.Button(self, text="Submit", command=self.on_button)
        self.label.pack()
        self.entry.pack()
        self.button.pack()
    def on_button(self):
        print(self.entry.get())


# Draw window
window = App()
window.title("Sleep Calculator")
window.geometry("360x640")
window.mainloop()

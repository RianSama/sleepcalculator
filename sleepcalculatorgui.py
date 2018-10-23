# Import modules
import tkinter

get = self.get()

'''def submit(b1):
    global age
    age = b1.get()'''


# Draw window
window = tkinter.Tk()
window.title("Sleep Calculator")
window.geometry("640x360")


l1 = tkinter.Label(window, text="How many years old are you?")
e1 = tkinter.Entry(window)
b1 = tkinter.Button(window, text="Submit", command=get)

print(a)

l1.pack()
e1.pack()
b1.pack()


window.mainloop()

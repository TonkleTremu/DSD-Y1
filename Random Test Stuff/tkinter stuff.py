from tkinter import *
from tkinter import ttk
from tkinter import filedialog

root = Tk()

def ReadStuff():
    print(the_theo_world.get()) # Reads the contents of "the_theo_world", such as if a user enters "Hello World!"

text_box = Label(root, text="Hello World!")
text_box.pack(side="left")
test_btn = Button(root, text="Read Text", command=ReadStuff)

the_theo_world = Entry(root)

root.geometry(f"{800}x{600}")

the_theo_world.pack()
test_btn.pack()

root.mainloop()
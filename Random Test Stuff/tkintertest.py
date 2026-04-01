from tkinter import *
from tkinter import ttk
from tkinter import filedialog

# The root of the application.
root = Tk()

# Sets up the "grid" for the stuff.
def AskForFile():
    MAX_USER_INPUT = 255
    # Reads a file, then displays its text, or an image.
    test = filedialog.askopenfile()
    try:
        new_image = PhotoImage(file=test.name)
        test_img.configure(image=new_image)
        test_img.image = new_image
    except:
        try:
            if(len(test.read()) <= MAX_USER_INPUT):
                text_box["text"] = test.read()
            else:
                raise(ValueError(1))
        except Exception as e:
            if(e == 1):
                text_box["text"] = "Please don't enter a text file over 255 characters in length."
            else:
                text_box["text"] = "Please only input a plain text file or image."

# A text and a button. Simple enough.
text_box = Label(root, text="Hello World!")
test_btn = Button(root, text="Open File", command=AskForFile)
image = PhotoImage(file="")
test_img = Label(root, image=image)


text_box.pack(side="left")
test_btn.pack()
test_img.pack()

root.mainloop()
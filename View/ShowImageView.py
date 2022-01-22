from tkinter import *
import tkinter as tk
from PIL import Image,ImageTk

class ShowImageView:
    def __init__(self, root, image = None):
        #Import tkinter library

        #Create an instance of tkinter frame
        win = tk.Toplevel(root);
        #Set the geometry
        win.geometry("750x550")
        #Load the image
        if (image == None):
            image = Image.open("./Images/test.jpg")
        #Convert To photoimage
        tkimage= ImageTk.PhotoImage(image)
        #Display the Image
        label=Label(win,image=tkimage)
        label.pack()

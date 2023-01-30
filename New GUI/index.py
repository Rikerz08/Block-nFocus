from tkinter import *
from PIL import Image
from Dashboard import *


#----------- Warning window
def Warning_Start(root):
    newwin = Toplevel()
    newwin.geometry("800x200")
    newwin.resizable(False, False)
    
    #making the window always pop up at the center of the screen
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    
    x = (screen_width / 2) - (800 / 2)
    y = (screen_height / 2 ) - (200 / 2)
    
    newwin.geometry(f'800x200+{int(x)}+{int(y)}')

    #placing the bg image by using label
    label2 = Label(newwin, image= warning)
    label2.place(x = 0, y = 0)
    
    #creating the Understand button
    button= Button(newwin, image=understood, command=lambda:[change(root)],borderwidth=0)
    button.grid(column=1, row=1, padx=311, pady=142)
    
   
    newwin.mainloop()
    
  
#switch window
def change(root):
    root.destroy()
    Dashboard()
    
#Making windows dimensions
def call():
    root = Tk()
  # Adjust size 
    root.geometry("800x500")
    root.resizable(False, False)
    root.title("Block'nFocus")
    
    #making the window always pop up at the center of the screen
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = (screen_width / 2) - (800 / 2)
    y = (screen_height / 2 ) - (500 / 2)

    root.geometry(f'800x500+{int(x)}+{int(y)}')
    
    #global variables to make it accessible
    global bg
    global click_btn
    global warning
    global understood

    bg = PhotoImage(file = "images/index.png")
    click_btn= PhotoImage(file='images/Start button.png')
    warning = PhotoImage(file='images/Warning 2.png')
    understood = PhotoImage(file='images/Understood.png')


    index(root)
    root.mainloop()

#running the index screen
def index(root):
    label1 = Label(root, image = bg)
    label1.place(x = 0, y = 0)

    text= Label(root, text= "")
    text.grid(column=0,row=0)

    #Let us create a dummy button and pass the image
    button= Button(root, image=click_btn,command=lambda:[Warning_Start(root)],borderwidth=0)
    button.grid(column=1, row=1, padx=460, pady=170)
    
    
call()
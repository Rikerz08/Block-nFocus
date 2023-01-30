from tkinter import *
from PIL import Image
from Dashboard import *
# Create object 
# root = Tk()
  
# # Adjust size 
# root.geometry("800x500")

# root.resizable(False, False)
#commands

#images


def Warning_Start(root):
    newwin = Toplevel()
    newwin.geometry("800x200")
    newwin.resizable(False, False)

    label2 = Label(newwin, image= warning)
    label2.place(x = 0, y = 0)
    
    button= Button(newwin, image=understood, command=lambda:[change(root)],borderwidth=0)
    button.grid(column=1, row=1, padx=311, pady=142)
    
   
    newwin.mainloop()
    
def change(root):
    root.destroy()
    Dashboard()
    

def call():
    root = Tk()
  # Adjust size 
    root.geometry("800x500")
    root.resizable(False, False)
    global bg
    global click_btn
    global warning
    global understood
    global Dashboard_bg
    global Block
    global Unblock
    bg = PhotoImage(file = "images/index.png")
    click_btn= PhotoImage(file='images/Start button.png')
    warning = PhotoImage(file='images/Warning 2.png')
    understood = PhotoImage(file='images/Understood.png')
    Dashboard_bg = PhotoImage(file='images/Dashboard.png')
    Block = PhotoImage(file='images/Block.png')
    Unblock = PhotoImage(file='images/Unblock.png')

    index(root)
    root.mainloop()

def index(root):
    label1 = Label(root, image = bg)
    label1.place(x = 0, y = 0)

    text= Label(root, text= "")
    text.grid(column=0,row=0)

    #Let us create a dummy button and pass the image
    button= Button(root, image=click_btn,command=lambda:[Warning_Start(root)],borderwidth=0)
    button.grid(column=1, row=1, padx=460, pady=170)
    
    
call()
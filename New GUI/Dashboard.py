from tkinter import *
# from PIL import Image
from pygame import *



def unblock(root):
    from Questions import Quiz
    root.destroy()
    Quiz()

def block(root):
    from BlockScreen import blockScreen
    root.destroy()
    blockScreen()


#Making windows dimensions
def dashboard():
    root = Tk()
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
    global Dashboard_bg
    global Block
    global Unblock

    Dashboard_bg = PhotoImage(file='images/Dashboard 4.png')
    Block = PhotoImage(file='images/Block.png')
    Unblock = PhotoImage(file='images/Unblock.png')

    Dashboard_start(root)
    root.mainloop()

#running the dashboard screen
def Dashboard_start(root):

    label3 = Label(root, image= Dashboard_bg)
    label3.place(x = 0, y = 0)

    
    button= Button(root, image=Block,borderwidth=0,command=lambda:[block(root)], bg="#FDFCDC")
    button.place(x = 200, y = 135)
    
    button2= Button(root, image=Unblock ,borderwidth=0,command=lambda:[unblock(root)], bg="#FDFCDC")
    button2.place(x=128,y=257)
    
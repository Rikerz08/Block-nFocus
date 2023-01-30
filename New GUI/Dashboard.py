from tkinter import *
from PIL import Image


# # def change(root):
# #     root.destroy()
# #     Dashboard_start()
    

def Dashboard():
    root = Tk()
    root.geometry("800x500")
    root.resizable(False, False)
    root.title("Block'nFocus")
    global Dashboard_bg
    global Block
    global Unblock

    Dashboard_bg = PhotoImage(file='images/Dashboard.png')
    Block = PhotoImage(file='images/Block.png')
    Unblock = PhotoImage(file='images/Unblock.png')

    Dashboard_start(root)
    root.mainloop()


def Dashboard_start(root):
    # root = Toplevel()
    label3 = Label(root, image= Dashboard_bg)
    label3.place(x = 0, y = 0)
    
    
    button= Button(root, image=Block,borderwidth=0, bg="#FDFCDC")
    # button.grid(column=1, row=1, padx=120, pady=50, rowspan=50)
    button.place(x = 200, y = 135)
    
    button2= Button(root, image=Unblock ,borderwidth=0, bg="#FDFCDC")
    button2.place(x=128,y=257)
    
    
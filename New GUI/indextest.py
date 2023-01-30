from tkinter import *
from PIL import ImageTk, Image
# Create object 
root = Tk()
  
# Adjust size 
root.geometry("800x500")

root.resizable(False, False)



def show_frame(frame):
    frame.tkraise()

bg = PhotoImage(file = "images/index.png")
click_btn= PhotoImage(file='images/Start button.png')
warning = PhotoImage(file='images/Warning 2.png')
understood = PhotoImage(file='images/Understood.png')
Dashboard_bg = PhotoImage(file='images/Dashboard.png')
Block = PhotoImage(file='images/Block.png')
Unblock = PhotoImage(file='images/Unblock.png')



frame1 = Frame(root)
frame2 = Frame(root)
frame3 = Frame(root)


label1 = Label(frame1, image = bg)
label1.place(x = 0, y = 0)



#add button Start
text= Label(frame1, text= "")
text.grid(column=0,row=0)

#Let us create a dummy button and pass the image
button = Button(frame1, image=click_btn, command=lambda:show_frame(frame2), borderwidth=0)
button.grid(column=1, row=1, padx=460, pady=170)


show_frame(frame1)


root.mainloop()
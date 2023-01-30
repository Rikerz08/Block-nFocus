from tkinter import *
from PIL import Image
  
# Create object 
root = Tk()
  
# Adjust size 
root.geometry("800x500")

root.resizable(False, False)
#commands


    
def Warning_Start():
    newwin = Toplevel()
    newwin.geometry("800x200")
    newwin.resizable(False, False)

    label2 = Label(newwin, image= warning)
    label2.place(x = 0, y = 0)
    
    button= Button(newwin, image=understood,command=lambda:([newwin.destroy(), Dashboard_start]),borderwidth=0)
    button.grid(column=1, row=1, padx=311, pady=142)
    
   
    newwin.mainloop()


def Dashboard_start():
    newwin = Toplevel()
    newwin.geometry("800x500")
    newwin.resizable(False, False)
    label3 = Label(newwin, image= Dashboard_bg)
    label3.place(x = 0, y = 0)
    
    
    button= Button(newwin, image=Block,command=Warning_Start ,borderwidth=0, bg="#FDFCDC")
    # button.grid(column=1, row=1, padx=120, pady=50, rowspan=50)
    button.place(x = 200, y = 135)
    
    button2= Button(newwin, image=Unblock,command=Warning_Start ,borderwidth=0, bg="#FDFCDC")
    button2.place(x=128,y=257)
    
    newwin.mainloop()
    

    
    


    
    
#images
bg = PhotoImage(file = "images/index.png")
click_btn= PhotoImage(file='images/Start button.png')
warning = PhotoImage(file='images/Warning 2.png')
understood = PhotoImage(file='images/Understood.png')
Dashboard_bg = PhotoImage(file='images/Dashboard.png')
Block = PhotoImage(file='images/Block.png')
Unblock = PhotoImage(file='images/Unblock.png')

# Add index background

label1 = Label(root, image = bg)
label1.place(x = 0, y = 0)



#add button Start


text= Label(root, text= "")
text.grid(column=0,row=0)

#Let us create a dummy button and pass the image
button= Button(root, image=click_btn,command=Warning_Start,borderwidth=0)
button.grid(column=1, row=1, padx=460, pady=170)


  
  
  
  
  
  
  
  
  
  
  
# Execute tkinter
root.mainloop()
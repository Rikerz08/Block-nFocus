from tkinter import *
# from PIL import Image
from pygame import *



def change(root):
    from Questions import Quiz
    root.destroy()
    Quiz()

def back(root):
    from Dashboard import dashboard
    root.destroy()
    dashboard()

def preset(root):
    from Preset import preset
    root.destroy()
    preset()


#Making windows dimensions
def blockScreen():
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
    
    global Block_bg
    global Preset
    global Write
    global Back
    Block_bg = PhotoImage(file='images/BlockBg.png')
    Preset =  PhotoImage(file='images/Preset.png')
    Write =  PhotoImage(file='images/Write.png')
    Back = PhotoImage(file='images/Back.png')


    BlockScreen_Start(root)
    root.mainloop()

#running the dashboard screen
def BlockScreen_Start(root):

    label3 = Label(root, image= Block_bg)
    label3.place(x = 0, y = 0)

    
    button= Button(root, image=Preset ,borderwidth=0,command=lambda:[preset(root)], bg="#FDFCDC", border=0)
    button.place(x = 235, y = 65)
    
    button2= Button(root, image=Write ,borderwidth=0,command=lambda:[change(root)], bg="#FDFCDC")
    button2.place(x=55,y=300)
     
    button3= Button(root, image=Back,borderwidth=0,command=lambda:[back(root)], bg="#FFFBFD", border=0)
    button3.place(x = 15, y = 27)



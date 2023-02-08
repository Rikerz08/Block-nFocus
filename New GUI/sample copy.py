from tkinter import *


def write():
    global root
    root = Tk()
    root.geometry("800x200")
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = (screen_width / 2) - (800 / 2)
    y = (screen_height / 2 ) - (200 / 2)
    
    root.geometry(f'800x200+{int(x)}+{int(y)}')
    
    global entry
    entry = Entry(root)
    entry.pack()
    global frame
    frame = Frame(root)
    frame.pack()
    
    global entries
    entries = []
    add_button = Button(root, text="Add Input", command=add_entry)
    add_button.pack()
    finish_button = Button(root, text="Finish", command=tba)
    finish_button.pack()

    global ErrorMsgBg
    global Okay

    ErrorMsgBg = PhotoImage(file='images/ErrorBg.png')
    Okay = PhotoImage(file='images/Okay.png')

    
    #List for storing the sites
    global siteList
    siteList = []
    print(siteList)
    root.mainloop()

def add_entry():
    global entry
    entry = Entry(frame)
    entry.pack()
    entries.append(entry)

def ErrorMsg():
    newwin = Toplevel(root)
    newwin.geometry("800x200")
    newwin.resizable(False, False)
    
    #making the window always pop up at the center of the screen
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    
    x = (screen_width / 2) - (800 / 2)
    y = (screen_height / 2 ) - (200 / 2)
    
    newwin.geometry(f'800x200+{int(x)}+{int(y)}')

    #placing the bg image by using label
    label2 = Label(newwin, image= ErrorMsgBg)
    label2.place(x = 0, y = 0)
    
    
    button= Button(newwin, image=Okay, command=lambda:[newwin.destroy()],borderwidth=0, background="#1E1A1A")
    button.place(x = 310, y = 138)
    
    newwin.mainloop()

def tba():
    global siteValue
    for site in entries:
        #this is to convert entry input into string
        siteValue = site.get()
        #if there is white space, validate it
        if " " in siteValue:
            ErrorMsg()
            # print(siteValue + " has a space in it. Please enter a valid input.")
        #append also a version without "www." and vice versa
        if siteValue != "exit" and "www." in siteValue:
            siteList.append(siteValue)
            siteList.append(siteValue.replace("www.",""))
        elif siteValue != 'exit' and "www." not in siteValue:
            siteList.append(siteValue)
            siteList.append("www." + siteValue)
    siteValue = entry.get()
    print("Got my niggas in paris")
    print(siteList)
    
write()
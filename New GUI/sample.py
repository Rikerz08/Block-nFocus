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
    
    # global entry
    entry1 = Entry(root)
    entry1.pack()
    global frame
    frame = Frame(root)
    frame.pack()
    
    global entries
    entries = [entry1]
    add_button = Button(root, text="Add Input", command=add_entry)
    add_button.pack()
    finish_button = Button(root, text="Finish", command=tba)
    finish_button.pack()

    global ErrorMsgBg
    global Okay

    ErrorMsgBg = PhotoImage(file='images/ErrorBg.png')
    Okay = PhotoImage(file='images/Okay.png')

    
    #List for storing the sites
    global entrySiteList
    entrySiteList = []
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
    from LogicFunctions import writeToHost
    global siteValue
    for site in entries:
        #this is to convert entry input into string
        siteValue = site.get()
        if len(siteValue) == 0:
            print("Please input something on field the blank field")
            ErrorMsg()
            return
        #if there is white space, validate it
        if " " in siteValue:
            print(siteValue + " has a space in it. Please enter a valid input.")
            ErrorMsg()
            return
        #append also a version without "www." and vice versa
        if siteValue != "exit" and "www." in siteValue:
            entrySiteList.append(siteValue)
            entrySiteList.append(siteValue.replace("www.",""))
        elif siteValue != 'exit' and "www." not in siteValue:
            entrySiteList.append(siteValue)
            entrySiteList.append("www." + siteValue)
    print(entrySiteList)
    noDupEntrySiteList = list(dict.fromkeys(entrySiteList))
    print(noDupEntrySiteList)
    writeToHost(noDupEntrySiteList)
    #Block of code for storing the sitelist into webstores.txt
    with open ("webstores.txt", "a+") as f:
        f.seek(0)
        f.writelines(' '.join(noDupEntrySiteList))
        f.write("\n")
    return
write()
from tkinter import *
import linecache

def preset():
    global root
    root = Tk()
    root.title('Codemy.com')
    root.geometry("800x500")
    root.resizable(False, False)
    
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = (screen_width / 2) - (800 / 2)
    y = (screen_height / 2 ) - (500 / 2)
    
    root.geometry(f'800x500+{int(x)}+{int(y)}')
    
    global preset_bg
    global Select
    global Delete
    global DeleteAll
    global WarningDelbg
    global WarningDelAllbg
    global Back
    global No
    global Yes
    global Selectbg
    global presetBlock
    preset_bg = PhotoImage(file='images/Presets.png')
    Select = PhotoImage(file='images/PresetSelect.png')
    presetBlock = PhotoImage(file='images/PresetBlock.png')
    Delete = PhotoImage(file='images/PresetDelete.png')
    DeleteAll = PhotoImage(file='images/PresetDeleteAll.png')
    WarningDelbg = PhotoImage(file='images/WarningDelete.png')
    WarningDelAllbg = PhotoImage(file='images/WarningDeleteAll.png')
    Selectbg = PhotoImage(file='images/Selectbg.png')
    No = PhotoImage(file='images/No.png')
    Yes = PhotoImage(file='images/Yes.png')
    Back = PhotoImage(file='images/Back.png')
    
    
    label3 = Label(root, image= preset_bg)
    label3.place(x = 0, y = 0)
    
    
    # Create frame and scrollbar
    my_frame = Frame(root)
    my_scrollbar = Scrollbar(my_frame, orient=VERTICAL)

    # Listbox!
    # SINGLE, BROWSE, MULTIPLE, EXTENDED
    global my_listbox
    my_listbox = Listbox(my_frame, width=53,height=8, yscrollcommand=my_scrollbar.set, font=('Times', 20), selectmode=SINGLE, borderwidth=0)

    #configure scrollbar
    my_scrollbar.config(command=my_listbox.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)
    my_frame.place(x = 22, y = 100)
    my_frame.configure(background="#FFFBFD")
    
    my_listbox.pack(pady=15)
    #This code is for getting the lines from the txt file and displaying them into the list box
    global presetList

    with open('webstores.txt', 'r') as f:
        presetList = [line.rstrip() for line in f]

    for item in presetList:
        my_listbox.insert(END, item)
    
    Preset_Start()
    
    root.mainloop()


def back():
    from BlockScreen import blockScreen
    root.destroy()
    blockScreen()
    
def DeleteWarn():
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
    label2 = Label(newwin, image= WarningDelbg)
    label2.place(x = 0, y = 0)
    
    #creating the Understand button
    button= Button(newwin, image=Yes, command=lambda:[delete(newwin)],borderwidth=0, background="#1E1A1A")
    button.place(x = 187, y = 138)
    
    button= Button(newwin, image=No, command=lambda:[newwin.destroy()],borderwidth=0, background="#1E1A1A")
    button.place(x = 430, y = 138)
    
    newwin.mainloop()

def SelectWarn():
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
    label2 = Label(newwin, image= Selectbg)
    label2.place(x = 0, y = 0)
    
    #creating the Understand button
    button= Button(newwin, image=Yes, command=lambda:[Select(newwin)],borderwidth=0, background="#1E1A1A")
    button.place(x = 187, y = 138)
    
    button= Button(newwin, image=No, command=lambda:[newwin.destroy()],borderwidth=0, background="#1E1A1A")
    button.place(x = 430, y = 138)
    
    newwin.mainloop()

def DeleteAllWarn():
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
    label2 = Label(newwin, image= WarningDelAllbg)
    label2.place(x = 0, y = 0)
    
    #creating the Understand button
    button= Button(newwin, image=Yes, command=lambda:[delete_all(newwin)],borderwidth=0, background="#1E1A1A")
    button.place(x = 187, y = 138)
    
    button= Button(newwin, image=No, command=lambda:[newwin.destroy()],borderwidth=0, background="#1E1A1A")
    button.place(x = 430, y = 138)
    
    newwin.mainloop()
        
def delete(a):
	#curselection will capture the current selection in the listbox by iterating thru it
	#then we assign the index to a variable in order for it to be deleted in webfile
    for item in my_listbox.curselection():
        delIndex = (item+1)
    lines = []
    # read file
    with open("webstores.txt", 'r') as fp:
		# read an store all lines into list
        lines = fp.readlines()
    # Write file
    with open("webstores.txt", 'w') as fp:
		# iterate each line
        for number, line in enumerate(lines):
			# delete line 5 and 8. or pass any Nth line you want to remove
			# note list index starts from 0
            if number not in [delIndex-1]:
                fp.write(line)
    a.destroy()
    my_listbox.delete(ANCHOR)
    # my_label.config(text='')

def select():
    from LogicFunctions import writeToHost, timeSet
    for item in my_listbox.curselection():
        delIndex = (item+1)
    currentPreset = linecache.getline("webstores.txt", delIndex)
    currentPresetList = currentPreset.split()
    # my_label.config(text=my_listbox.get(ANCHOR))
    writeToHost(currentPresetList)
    print("WRITTEN TO HOST")

def delete_all(a):
    with open('webstores.txt', 'w') as f:
        f.truncate(0)
    a.destroy()
    my_listbox.delete(0, END)

def select_all():
	result = ''

	for item in my_listbox.curselection():
		result = result + str(my_listbox.get(item)) + '\n'

	my_label.config(text=result)

def delete_multiple():
	for item in reversed(my_listbox.curselection()):
		my_listbox.delete(item)
		my_label.config(text='')
  
def Preset_Start():
   
    # my_button = Button(root, text="Delete", command=delete)
    # my_button.pack(pady=10)
    button1= Button(root, image=presetBlock,borderwidth=0,command=SelectWarn, bg="#FDFCDC")
    button1.place(x = 55, y = 400)
    
    button2= Button(root, image=Delete,borderwidth=0,command=DeleteWarn, bg="#FDFCDC")
    button2.place(x = 318, y = 400)
    
    button3= Button(root, image=DeleteAll,borderwidth=0,command=DeleteAllWarn, bg="#FDFCDC")
    button3.place(x = 578, y = 400)
    
    button4= Button(root, image=Back,borderwidth=0,command=back, bg="#FFFBFD", border=0)
    button4.place(x = 53, y = 53)


    # my_button2 = Button(root, text="Select", command=select)
    # my_button2.pack(pady=10)
    

    # global my_label
    # my_label = Label(root, text='')
    # my_label.pack(pady=5)

    # my_button3 = Button(root, text="Delete All", command=delete_all)
    # my_button3.pack(pady=10)

    # my_button4 = Button(root, text="Select All", command=select_all)
    # my_button4.pack(pady=10)

    # my_button5 = Button(root, text="Delete Multiple", command=delete_multiple)
    # my_button5.pack(pady=10)



######################################################################################################################################################################################
# preset()
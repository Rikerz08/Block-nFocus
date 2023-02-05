from tkinter import *


def Preset():
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
    
    global Dashboard_bg
    Dashboard_bg = PhotoImage(file='images/Dashboard 3.png')
    label3 = Label(root, image= Dashboard_bg)
    label3.place(x = 0, y = 0)
    
    
    # Create frame and scrollbar
    my_frame = Frame(root)
    my_scrollbar = Scrollbar(my_frame, orient=VERTICAL)

    # Listbox!
    # SINGLE, BROWSE, MULTIPLE, EXTENDED
    global my_listbox
    my_listbox = Listbox(my_frame, width=55,height=9, yscrollcommand=my_scrollbar.set, font=('Times', 20), selectmode=SINGLE, borderwidth=0)

    #configure scrollbar
    my_scrollbar.config(command=my_listbox.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)
    my_frame.place(x = 5, y = 20)
    
    
    
    
    global my_list
    my_listbox.pack(pady=15)
    
    my_list = ["One", "Two", "Three", "One", "Two", "Three", "One", "Two", "Three", "One", "Two", "Three", "One", "Two", "Three", "One", "Two", "Three", "One", "Two", "Three", "One", "Two", "Three", ]

    for item in my_list:
        my_listbox.insert(END, item)
    
    Preset_Start()
    
    root.mainloop()
    
    
def delete():
    my_listbox.delete(ANCHOR)
    my_label.config(text='')

def select():
	my_label.config(text=my_listbox.get(ANCHOR))

def delete_all():
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
   
    
    my_button = Button(root, text="Delete", command=delete)
    my_button.pack(pady=10)

    my_button2 = Button(root, text="Select", command=select)
    my_button2.pack(pady=10)

    global my_label
    my_label = Label(root, text='')
    my_label.pack(pady=5)

    my_button3 = Button(root, text="Delete All", command=delete_all)
    my_button3.pack(pady=10)

    my_button4 = Button(root, text="Select All", command=select_all)
    my_button4.pack(pady=10)

    my_button5 = Button(root, text="Delete Multiple", command=delete_multiple)
    my_button5.pack(pady=10)

Preset()
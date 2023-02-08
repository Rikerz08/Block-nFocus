from tkinter import *
import linecache

root = Tk()
root.title('Codemy.com')
root.geometry("800x500")

# Create frame and scrollbar
my_frame = Frame(root)
my_scrollbar = Scrollbar(my_frame, orient=VERTICAL)

# Listbox!
# SINGLE, BROWSE, MULTIPLE, EXTENDED
my_listbox = Listbox(my_frame, width=100, yscrollcommand=my_scrollbar.set, selectmode=EXTENDED)

#configure scrollbar
my_scrollbar.config(command=my_listbox.yview)
my_scrollbar.pack(side=RIGHT, fill=Y)
my_frame.pack()

my_listbox.pack(pady=15)




# #Add item to listbox
# my_listbox.insert(END, "This is an item")
# my_listbox.insert(END, "Second Item!")
# presetList = ["1231231231", "LET ME GO HOME"]
# Add list of items
with open('webstores.txt', 'r') as f:
	presetList = [line.rstrip() for line in f]

for item in presetList:
	my_listbox.insert(END, item)

def delete():
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
	my_listbox.delete(ANCHOR)
	my_label.config(text='')
	# return
	#find the index of the element in the list that contains the text in the anchor
	#and then do the listcache to get the line number (index + 1) and delete the line from file.

def select():
	my_label.config(text=my_listbox.get(ANCHOR))

def delete_all():
	with open("webstores.txt", 'w') as fp:
		# read an store all lines into list
		fp.truncate(0)
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

root.mainloop()

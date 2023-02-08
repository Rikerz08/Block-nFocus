import tkinter as tk

def add_entry():
    entry = tk.Entry(frame)
    entry.pack()
    entries.append(entry)

def tba():
    from Preset import ErrorMsg
    global siteValue
    for site in entries:
        #this is to convert entry input into string
        siteValue = site.get()
        #if there is white space, validate it
        if " " in siteValue:
            print(siteValue + " has a space in it. Please enter a valid input.")
            break
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

root = tk.Tk()
entry = tk.Entry(root)
entry.pack()
frame = tk.Frame(root)
frame.pack()
entries = []
add_button = tk.Button(root, text="Add Input", command=add_entry)
add_button.pack()
finish_button = tk.Button(root, text="Finish", command=tba)
finish_button.pack()

#List for storing the sites
siteList = []
print(siteList)
root.mainloop()
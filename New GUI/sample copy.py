import tkinter as tk

root = tk.Tk()
root.title("Dynamic Scrollable Frame Example")

# Create a canvas to hold the frame
canvas = tk.Canvas(root)
canvas.pack(side="left", fill="both", expand=True)

# Create a vertical scrollbar for the canvas
scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
scrollbar.pack(side="right", fill="y")

# Connect the canvas to the scrollbar
canvas.configure(yscrollcommand=scrollbar.set)

# Create a frame to hold the input fields
frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=frame, anchor="nw")

# Create the input fields
entries = []
for i in range(100):
    entry = tk.Entry(frame)
    entry.pack(fill="x")
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

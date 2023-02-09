import tkinter as tk

def add_entry():
    entry = tk.Entry(frame)
    entry.pack()
    entries.append(entry)

def remove_entry():
    if entries:
        entry = entries.pop()
        entry.pack_forget()

root = tk.Tk()
root.geometry("800x500")

frame = tk.Frame(root)
frame.pack()

entries = []
add_button = tk.Button(root, text="Add Entry", command=add_entry)
add_button.pack()
remove_button = tk.Button(root, text="Remove Entry", command=remove_entry)
remove_button.pack()

root.mainloop()

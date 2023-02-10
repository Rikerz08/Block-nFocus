import tkinter as tk
from tkinter import ttk

def add_entry():
        
    entry = tk.Entry(inner_frame, width=50, font=("Helvetica", 20))
    entry.place(relx=0.5, rely=0, anchor='n', x=0, y=0)

    entries.append(entry)
    app.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

def remove_entry():
    
    if entries:
        entry = entries.pop()
        entry.pack_forget()
        app.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))

def DynamicEntryBoxes():
    global app
    app = tk.Tk()
    app.title("Dynamic Entry Boxes")
    app.geometry("800x500")
    app.resizable(False, False)
    

    frame = tk.Frame(app)
    frame.place(relx=0.5, rely=0.5, anchor='center', width=800, height=500)
    

    scrollbar = ttk.Scrollbar(frame)
    scrollbar.place(relx=0.95, rely=0.5, anchor='center', width=20, height=500)

    global canvas
    canvas = tk.Canvas(frame, yscrollcommand=scrollbar.set)
    canvas.place(relx=0.5, rely=0.5, anchor='center', width=780, height=500)
    canvas.config(scrollregion=canvas.bbox("all"))
    

    scrollbar.config(command=canvas.yview)

    global inner_frame
    inner_frame = tk.Frame(canvas)
    canvas.create_window((0, 0), window=inner_frame, anchor='nw')
    
    entry1 = tk.Entry(inner_frame, width=50, font=("Helvetica", 20))
    entry1.place(relx=0.5, rely=0, anchor='n', x=0, y=0)
    global entries
    entries = [entry1]
    start()
    
    app.mainloop()


def start():
    add_entry_button = tk.Button(app, text="Add Entry", command=add_entry)
    add_entry_button.place(relx=0.5, rely=0.95, anchor='s', x=0, y=0)

    remove_entry_button = tk.Button(app, text="Remove Entry", command=remove_entry)
    remove_entry_button.place(relx=0.5, rely=0.9, anchor='s', x=0, y=0)

    canvas.create_window((0, 0), window=inner_frame, anchor='nw')
    canvas.config(scrollregion=canvas.bbox("all"))

DynamicEntryBoxes()
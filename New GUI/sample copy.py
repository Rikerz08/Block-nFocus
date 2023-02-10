# import tkinter as tk

# root = tk.Tk()
# root.title("Dynamic Scrollable Frame Example")

# # Create a canvas to hold the frame
# canvas = tk.Canvas(root)
# canvas.pack(side="left", fill="both", expand=True)

# # Create a vertical scrollbar for the canvas
# scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
# scrollbar.pack(side="right", fill="y")

# # Connect the canvas to the scrollbar
# canvas.configure(yscrollcommand=scrollbar.set)

# # Create a frame to hold the input fields
# frame = tk.Frame(canvas)
# canvas.create_window((0, 0), window=frame, anchor="nw")

# # Create the input fields
# entries = []
# for i in range(100):
#     entry = tk.Entry(frame)
#     entry.pack(fill="x")
#     entries.append(entry)

# def tba():
#     from Preset import ErrorMsg
#     global siteValue
#     for site in entries:
#         #this is to convert entry input into string
#         siteValue = site.get()
#         #if there is white space, validate it
#         if " " in siteValue:
#             print(siteValue + " has a space in it. Please enter a valid input.")
#             break
#         #append also a version without "www." and vice versa
#         if siteValue != "exit" and "www." in siteValue:
#             siteList.append(siteValue)
#             siteList.append(siteValue.replace("www.",""))
#         elif siteValue != 'exit' and "www." not in siteValue:
#             siteList.append(siteValue)
#             siteList.append("www." + siteValue)
#     siteValue = entry.get()
#     print("Got my niggas in paris")
#     print(siteList)

# root = tk.Tk()
# entry = tk.Entry(root)
# entry.pack()
# frame = tk.Frame(root)
# frame.pack()
# entries = []
# add_button = tk.Button(root, text="Add Input", command=add_entry)
# add_button.pack()
# finish_button = tk.Button(root, text="Finish", command=tba)
# finish_button.pack()

# #List for storing the sites
# siteList = []
# print(siteList)
# root.mainloop()


####SAVED
# import tkinter as tk
# from tkinter import ttk

# class DynamicEntryBoxes(tk.Tk):
#     def __init__(self, *args, **kwargs):
#         tk.Tk.__init__(self, *args, **kwargs)
#         self.title("Dynamic Entry Boxes")
#         self.geometry("300x400")
#         self.resizable(False, False)

#         self.frame = tk.Frame(self)
#         self.frame.pack(expand=True, fill='both')

#         self.entries = []
#         self.scrollbar = ttk.Scrollbar(self.frame)
#         self.scrollbar.pack(side='right', fill='y')

#         self.canvas = tk.Canvas(self.frame, yscrollcommand=self.scrollbar.set)
#         self.canvas.pack(side='left', fill='both', expand=True)

#         self.scrollbar.config(command=self.canvas.yview)

#         self.inner_frame = tk.Frame(self.canvas)
#         self.canvas.create_window((0,0), window=self.inner_frame, anchor='nw')

#         self.add_entry_button = tk.Button(self, text="Add Entry", command=self.add_entry)
#         self.add_entry_button.pack(side='bottom', pady=5)

#         self.remove_entry_button = tk.Button(self, text="Remove Entry", command=self.remove_entry)
#         self.remove_entry_button.pack(side='bottom', pady=5)

#         self.update_idletasks()
#         self.canvas.config(scrollregion=self.canvas.bbox("all"))

#     def add_entry(self):
#         entry = tk.Entry(self.inner_frame)
#         entry.pack(side='top', fill='x')
#         self.entries.append(entry)
#         self.update_idletasks()
#         self.canvas.config(scrollregion=self.canvas.bbox("all"))

#     def remove_entry(self):
#         if self.entries:
#             entry = self.entries.pop()
#             entry.pack_forget()
#             self.update_idletasks()
#             self.canvas.config(scrollregion=self.canvas.bbox("all"))

# if __name__ == '__main__':
#     app = DynamicEntryBoxes()
#     app.mainloop()
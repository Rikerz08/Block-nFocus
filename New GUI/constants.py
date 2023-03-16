import tkinter as tk;
global root

root = tk.Tk()
# Adjust size 
root.geometry("800x500")
root.resizable(False, False)
root.title("Block'nFocus")

def displayPage(page):
    deletePage()
    page()

def deletePage():
    for frame in mainFrame.winfo_children():
        frame.destroy()

global mainFrame

mainFrame = tk.Frame(root)
mainFrame.pack()
mainFrame.propagate(False)
mainFrame.configure(width = 800, height = 500)

bg = tk.PhotoImage(file = "images/index.png")
click_btn= tk.PhotoImage(file='images/Start button.png')



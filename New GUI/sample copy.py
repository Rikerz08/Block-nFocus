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

root.mainloop()

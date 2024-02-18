# main.py
import tkinter as tk
from gui import create_gui

# Create the main application window
app = tk.Tk()
app.title("ID Card Generator")

# Create and place labels and entry fields
create_gui(app)

# Run the GUI application
app.mainloop()

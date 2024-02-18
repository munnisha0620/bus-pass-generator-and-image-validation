# gui.py
from tkinter import filedialog
import tkinter as tk
from tkinter import messagebox
from id_card_generator import generate_id_card

def create_gui(app):
    # Create and place labels and entry fields
    name_label = tk.Label(app, text="Name:")
    name_label.grid(row=0, column=0)
    name_entry = tk.Entry(app)
    name_entry.grid(row=0, column=1)

    reg_number_label = tk.Label(app, text="Reg. Number:")
    reg_number_label.grid(row=1, column=0)
    reg_number_entry = tk.Entry(app)
    reg_number_entry.grid(row=1, column=1)

    year_of_study_label = tk.Label(app, text="Year of Study:")
    year_of_study_label.grid(row=2, column=0)
    year_of_study_entry = tk.Entry(app)
    year_of_study_entry.grid(row=2, column=1)

    boarding_point_label = tk.Label(app, text="Boarding Point:")
    boarding_point_label.grid(row=3, column=0)
    boarding_point_entry = tk.Entry(app)
    boarding_point_entry.grid(row=3, column=1)

    phone_number_label = tk.Label(app, text="Phone Number:")
    phone_number_label.grid(row=4, column=0)
    phone_number_entry = tk.Entry(app)
    phone_number_entry.grid(row=4, column=1)

    email_label = tk.Label(app, text="Email:")
    email_label.grid(row=5, column=0)
    email_entry = tk.Entry(app)
    email_entry.grid(row=5, column=1)

    branch_label = tk.Label(app, text="Branch:")
    branch_label.grid(row=6, column=0)
    branch_entry = tk.Entry(app)
    branch_entry.grid(row=6, column=1)

    passport_photo_label = tk.Label(app, text="Passport Photo:")
    passport_photo_label.grid(row=7, column=0)
    passport_photo_entry = tk.Entry(app)
    passport_photo_entry.grid(row=7, column=1)
    select_passport_photo_button = tk.Button(app, text="Select", command=select_passport_photo)
    select_passport_photo_button.grid(row=7, column=2)

    challan_photo_label = tk.Label(app, text="Challan Photo:")
    challan_photo_label.grid(row=8, column=0)
    challan_photo_entry = tk.Entry(app)
    challan_photo_entry.grid(row=8, column=1)
    select_challan_photo_button = tk.Button(app, text="Select", command=select_challan_photo)
    select_challan_photo_button.grid(row=8, column=2)

    generate_button = tk.Button(app, text="Generate ID Card", command=generate_id_card)
    generate_button.grid(row=9, columnspan=2)

# Function to open a file dialog for selecting passport size photo
def select_passport_photo():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    passport_photo_entry.delete(0, tk.END)
    passport_photo_entry.insert(0, file_path)

# Function to open a file dialog for selecting challan photo
def select_challan_photo():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    challan_photo_entry.delete(0, tk.END)
    challan_photo_entry.insert(0, file_path)

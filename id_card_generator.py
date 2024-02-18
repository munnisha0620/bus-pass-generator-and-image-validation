# id_card_generator.py
from tkinter import messagebox
import pandas as pd
from PIL import Image, ImageDraw, ImageFont
import qrcode
import os
import re
from email_sender import send_email_with_id_card
from fee_validator import validate_fee_structure

# Specify the base directory where you want to save files
base_directory = "C:\\Users\\THARIMUNNISHA\\Downloads\\fuel project"

# Define the destination fee (replace with the actual destination fee)
destination_fee = 16422

# Load the fee structure from an Excel sheet
fee_structure_df = pd.read_excel("fee_structure.xlsx")  # Replace with the actual file path

# Load the existing user details from the Excel file (if it exists)
user_details_file = f"{base_directory}\\user_details.xlsx"
if os.path.exists(user_details_file):
    user_details_df = pd.read_excel(user_details_file)
else:
    # Create a new DataFrame if the file doesn't exist
    user_details_df = pd.DataFrame(columns=["Name", "Reg. Number", "Year of Study", "Boarding Point", "Phone Number", "Email", "Branch", "QR Code Sent"])

def validate_phone_and_email(phone_number, email):
    if not (re.match(r"^\d{10}$", phone_number) and re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zAZ0-9-.]+$", email)):
        return False
    return True

def generate_id_card(name, reg_number, year_of_study, boarding_point, phone_number, email, branch, passport_photo_path, challan_photo_path):
    # Validate phone number and email
    if not validate_phone_and_email(phone_number, email):
        messagebox.showerror("Error", "Invalid phone number or email address.")
        return

    # Validate the registration number format (3 digits, 2 letters, 5 digits)
    if not re.match(r"^\d{3}[a-zA-Z]{2}\d{5}$", reg_number):
        messagebox.showerror("Error", "Invalid registration number format.")
        return

    # Validate the year of study (less than or equal to 4)
    if not year_of_study.isdigit() or int(year_of_study) > 4:
        messagebox.showerror("Error", "Invalid year of study. Please enter a value less than or equal to 4.")
        return

    # Store the user details in a dictionary
    user_details = {
        "Name": name,
        "Reg. Number": reg_number,
        "Year of Study": year_of_study,
        "Boarding Point": boarding_point,
        "Phone Number": phone_number,
        "Email": email,
        "Branch": branch,
        "Bus pass Sent": "Not Sent"
    }

    # Append the new user details to the existing DataFrame
    user_details_df = user_details_df.append(user_details, ignore_index=True)

    # Save the updated user details in the Excel file
    user_details_df.to_excel(user_details_file, index=False)

     # Save the ID card image with the registration number as the filename
    id_card_filename = f"{base_directory}\\E-bus pass\\{reg_number}.png"
    image.save(id_card_filename)

    # Add a QR code with the user details
    generate_qr_code(details, id_card_filename)

    # Display the generated ID card
    image.show()

    # Check if the total amount and boarding point match the predefined fee structure
    if validate_fee_structure(reg_number, destination_fee):
        # Send a copy of the ID card to the entered email
        email_sent = send_email_with_id_card(email, id_card_filename)
        if email_sent:
            # Update the user details DataFrame to indicate that the QR code has been sent
            user_details_df.loc[user_details_df['Reg. Number'] == reg_number, 'QR Code Sent'] = "Sent"
            user_details_df.to_excel(f"{base_directory}\\user_details.xlsx", index=False)
            messagebox.showinfo("Success", "ID card generated and sent to your email.")
        else:
            messagebox.showerror("Error", "Failed to send the email.")
    else:
        messagebox.showerror("Error", "Full payment not done or boarding point mismatch.")

    # Check if the total amount and boarding point match the predefined fee structure
    if validate_fee_structure(reg_number, destination_fee):
        # Send a copy of the ID card to the entered email
        email_sent = send_email_with_id_card(email, id_card_filename)
        if email_sent:
            # Update the user details DataFrame to indicate that the QR code has been sent
            user_details_df.loc[user_details_df['Reg. Number'] == reg_number, 'QR Code Sent'] = "Sent"
            user_details_df.to_excel(f"{base_directory}\\user_details.xlsx", index=False)
            messagebox.showinfo("Success", "ID card generated and sent to your email.")
        else:
            messagebox.showerror("Error", "Failed to send the email.")
    else:
        messagebox.showerror("Error", "Full payment not done or boarding point mismatch.")

# ... (rest of the file, including UI components and main loop)

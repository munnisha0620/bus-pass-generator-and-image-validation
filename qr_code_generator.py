# id_card_generator.py
from tkinter import messagebox
import pandas as pd
from PIL import Image, ImageDraw, ImageFont
import qrcode
import os
from email_sender import send_email_with_id_card
from fee_validator import validate_fee_structure

# ... (other imports and global variables)

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

    # Load the existing user details from the Excel file (if it exists)
    user_details_file = f"{base_directory}\\user_details.xlsx"
    if os.path.exists(user_details_file):
        user_details_df = pd.read_excel(user_details_file)
    else:
        # Create a new DataFrame if the file doesn't exist
        user_details_df = pd.DataFrame(columns=["Name", "Reg. Number", "Year of Study", "Boarding Point", "Phone Number", "Email", "Branch", "QR Code Sent"])

    # Append the new user details to the existing DataFrame
    user_details_df = user_details_df.append(user_details, ignore_index=True)

    # Save the updated user details in the Excel file
    user_details_df.to_excel(user_details_file, index=False)

    # Create a blank image with a blue border
    card_width = 400
    card_height = 250
    border_size = 10
    inner_margin = 10
    image = Image.new("RGB", (card_width, card_height), "white")
    draw = ImageDraw.Draw(image)

    # Add a blue border
    draw.rectangle([(0, 0), (card_width, card_height)], outline="blue", width=border_size)

    # Load the logo
    logo = Image.open("C:\\Users\\THARIMUNNISHA\\Downloads\\fuel project\\logo.png")

    # Calculate the height for fitting the logo in 30% of the image from the top
    logo_height = int(0.3 * card_height)

    # Calculate the width to maintain the aspect ratio
    logo_width = int((logo_height / logo.size[1]) * logo.size[0])

    # Resize and paste the logo on top
    logo = logo.resize((logo_width, logo_height))
    image.paste(logo, (border_size + (card_width - logo_width) // 2, border_size))

    # Add the passport size photo
    if passport_photo_path:
        passport_photo = Image.open(passport_photo_path)
        passport_photo = passport_photo.resize((70, 70))
        image.paste(passport_photo, (border_size + inner_margin, logo_height + inner_margin))

    # Add the user details to the generated image
    details = f"Name: {name}\nReg. Number: {reg_number}\nYear of Study: {year_of_study}\nBoarding Point: {boarding_point}\nBranch: {branch}"
    details_font = ImageFont.load_default()
    draw.multiline_text((border_size + inner_margin * 2 + 70, logo_height + inner_margin), details, fill=(0, 0, 0), font=details_font)

    # Save the ID card image with the registration number as the filename
    id_card_filename = f"{base_directory}\\E-bus pass\\{reg_number}.png"
    image.save(id_card_filename)

    # Add a QR code with the user details
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=4,
        border=4,
    )
    qr.add_data(details)
    qr.make(fit=True)
    qr_image = qr.make_image(fill_color="black", back_color="white")
    qr_image = qr_image.resize((90, 90))
    image.paste(qr_image, (border_size + inner_margin * 3 + 70 * 2, logo_height + inner_margin))

    # Save the ID card image with the registration number as the filename
    image.save(id_card_filename)

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

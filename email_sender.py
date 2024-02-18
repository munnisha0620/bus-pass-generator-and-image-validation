# email_sender.py
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import os

def send_email_with_id_card(email, id_card_path):
    try:
        from_email = "buspassdemovignan@gmail.com"
        password = "Vignan123"

        # Create an SMTP server
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(from_email, password)

        msg = MIMEMultipart()
        msg["From"] = from_email
        msg["To"] = email
        msg["Subject"] = "Your Bus Pass ID Card"

        text = MIMEText("Please find your Bus Pass ID Card attached.")
        msg.attach(text)

        with open(id_card_path, "rb") as f:
            img_data = MIMEImage(f.read(), name=os.path.basename(id_card_path))
            msg.attach(img_data)

        server.sendmail(from_email, email, msg.as_string())
        server.quit()
        return True
    except Exception as e:
        return False

"""Module providing a function otp generation function."""
import smtplib
import random
import string
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email configuration
SENDER_EMAIL = "akiwelekar@gmail.com"
SENDER_PASSWORD = "pxue ssll qagm chhu"
RECEIVER = "awk@dbatu.ac.in"




def generate_otp(l):
    """Generate a random 6-digit OTP."""
    return ''.join(random.choice(string.digits) for _ in range(l))

def send_otp_mail(pwd):
    """Generate a random 6-digit OTP."""
    subject = "Your OTP Code"
    message = f"Your OTP code is: {pwd}"

    # Setup the email server
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)

        # Create and send the email
        msg = MIMEMultipart()
        msg['From'] = SENDER_EMAIL
        msg['To'] = RECEIVER
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))

        server.sendmail(SENDER_EMAIL, RECEIVER, msg.as_string())
        server.quit()

        print(f"OTP sent to {RECEIVER}")

    except smtplib.SMTPException as e:
        print(f"An error occurred: {e}")

# Generate OTP

send_otp_mail( generate_otp(6))

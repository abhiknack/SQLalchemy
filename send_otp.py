from random import randint
import smtplib
from email.mime.text import MIMEText
from main import session

from psycopg2 import DataError, IntegrityError

from tables import User

def send_otp(data):
    try:
        passcode = session.query(User).filter_by(email=data['email']).first()
        subject = "Hostel 17 PassCode"
        body = f"Your PassCode is {passcode}"
        sender = "abhibhai1507@gmail.com"
        recipients = [data['email']]
        password = "mnmb rtil xyzj eain"


        def send_email(subject, body, sender, recipients, password):
            msg = MIMEText(body)
            msg['Subject'] = subject
            msg['From'] = sender
            msg['To'] = ', '.join(recipients)
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
                smtp_server.login(sender, password)
                smtp_server.sendmail(sender, recipients, msg.as_string())
                print("Message sent!")
        send_email(subject, body, sender, recipients, password)
    except IntegrityError as e:
        # Handle integrity-related errors (e.g., unique constraint violation)
        session.rollback()
        return {"status": "error", "message": f"IntegrityError: {str(e)}"}

    except DataError as e:
        # Handle data-related errors (e.g., incorrect data type)
        session.rollback()
        return {"status": "error", "message": f"DataError: {str(e)}"}

    except Exception as e:
        # Handle other exceptions
        session.rollback()
        return {"status": "error", "message": f"An unexpected error occurred: {str(e)}"}

        

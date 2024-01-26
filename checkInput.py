from psycopg2 import DataError, IntegrityError
from sqlalchemy import exists
from main import session
from tables import User
from validate_email_address import validate_email
def check_input(data):
    roll_exists = ''  # Default value
    rollno_exists = ''
    mail_exists = ''
    email_exists = ''
    username_exists = ''
    user_exists = ''
    try:
        if data["roll"]:
            roll_exists = not session.query(exists().where(User.roll == data["roll"])).scalar()
            rollno_exists = f" this roll no. is {'available.'if roll_exists else 'not available.'}"
        if data["username"]:
            user_exists =not session.query(exists().where(User.username == data["username"])).scalar()
            username_exists = f" this username is {'available.'if user_exists else 'not available.'}"
        if validate_email(data["email"]):
            if data["email"]:
                mail_exists =not session.query(exists().where(User.roll == data["roll"])).scalar()
                email_exists = f" this email is {'available.'if mail_exists else 'not available.'}"
            else:
                email_exists="Not a valid email"
        
        result_dict = {
            "username": {'state':user_exists,
                        'text':username_exists},
            "rollno":  {'state':roll_exists,
                        'text':rollno_exists},
            "email": {'state':mail_exists,
                        'text':email_exists}
        }
        return result_dict
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
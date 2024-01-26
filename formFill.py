from random import randint
from psycopg2 import DataError, IntegrityError
from main import session
from tables import User

def add_user(data):
    try:
        pass_code = randint(1000, 9999)
        session.add(User(email=data['email'], roll=data['roll'], username=data['username'],passcode=pass_code))
        session.commit()
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

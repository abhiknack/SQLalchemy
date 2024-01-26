from psycopg2 import DataError, IntegrityError
from tables import User,Comment
from main import session

def insert_comment(data):
    try:
        # Assuming Comment and User classes are defined somewhere
        comment = Comment(
            comment=data['comment'],
            rating=data['rating'],
            author=User(username=data['username']),
            dishes_id=data['dishes_id']
        )
        
        session.add(comment)
        session.commit()
        return {"status": "success", "message": "Comment added successfully"}

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
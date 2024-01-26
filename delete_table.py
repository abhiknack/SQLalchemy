from connect import engine  # Assuming 'engine' is created in 'connect.py'
from tables import Day,MealType,Dish,User,Comment
# Specify the table name you want to delete
def delete_tables():
    try:
        Comment.__table__.drop(engine)
        Dish.__table__.drop(engine)
        Day.__table__.drop(engine)
        User.__table__.drop(engine)
        MealType.__table__.drop(engine)
        return {"status": "success", "message": "Tables dropped successfully"}
    except :
        return {"status": "error"}



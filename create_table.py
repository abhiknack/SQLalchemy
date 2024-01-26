from tables import Base,Day,Dish,MealType
from connect import engine


print("CREATING TABLES >>>> ")
def create_table():
    try:
        Base.metadata.create_all(bind=engine)
        return {"status": "success", "message": "Tables Created Successfully"}
    except:
        return {"status": "error"}
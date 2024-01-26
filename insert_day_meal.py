from tables import Day,MealType,Dish
from main import session

def insert_day_meal():
    try:
        new_days = [Day(day_name='Sunday'),Day(day_name='Monday'), Day(day_name='Tuesday'), Day(day_name='Wednesday'),Day(day_name='Thursday'),Day(day_name='Friday'),Day(day_name='Saturday')]
        meal_types = [MealType(meal_type_name='BreakFast'),MealType(meal_type_name='Lunch'),MealType(meal_type_name='Snacks'),MealType(meal_type_name='Dinner')]
        session.add_all(new_days)
        session.add_all(meal_types)
        session.commit()
        return {"status": "success", "message": "daymeal added successfully"}
    except:
        return {"status": "error"}




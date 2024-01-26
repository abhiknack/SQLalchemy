from main import session
from tables import Dish
# Create a dictionary to organize dishes by day and meal type
def get_menu():
    try:
        dishes = session.query(Dish).all()
        days_data = {}

        for dish in dishes:
            day_name = dish.day.day_name
            meal_type_name = dish.mealtype.meal_type_name

            if day_name not in days_data:
                days_data[day_name] = {}

            if meal_type_name not in days_data[day_name]:
                days_data[day_name][meal_type_name] = {}

            if "dishes" not in days_data[day_name][meal_type_name]:
                days_data[day_name][meal_type_name]["dishes"] = dish.dishes
                days_data[day_name][meal_type_name]["keys"] = dish.dishes_id

        return days_data

    except Exception as e:
        # Handle the exception as needed
        return {"error": f"An unexpected error occurred: {str(e)}"}

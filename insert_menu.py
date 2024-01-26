from io import BytesIO
from fastapi import File, UploadFile
from tables import Day,MealType,Dish
from main import session
import pandas as pd
def insert_menu(file: UploadFile = File(...)):
    try:
        df = pd.read_excel(BytesIO(file.file.read())).fillna('')
        days = ['SUNDAY','MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY']
        meal_types = ['BREAKFAST','LUNCH','SNACKS','DINNER']
        for day in range(len(days)):
            col = df.columns.get_loc(days[day])
            row = df[df.iloc[:, 0] == meal_types[0] ].index[0]
            session.add(Dish(dishes={
                "Main Dish": [df.iloc[row,col].replace('+', ''),df.iloc[row+1,col].replace('+', '') ],
                    "Egg / Cereals": df.iloc[row+2,col].replace('+', ''),
                    "Sprouts": df.iloc[row+3,col].replace('+', ''),
                    "Tea and Coffee": df.iloc[row+4,col].replace('+', ''),
                    "Fruit": df.iloc[row+5,col].replace('+', ''),
                    "Milk": df.iloc[row+6,col].replace('+', '')
            },meal_type_id=1,day_id=day+1))
            row = df[df.iloc[:, 0] == meal_types[1] ].index[0]
            session.add(Dish(dishes={
                "Dry":df.iloc[row,col].replace('+', '') ,
                    "Gravy": df.iloc[row+1,col].replace('+', ''),
                    "Sp Rice": df.iloc[row+2,col].replace('+', ''),
                    "India Bread": df.iloc[row+3,col].replace('+', ''),
                    "Pickle": df.iloc[row+4,col].replace('+', ''),
                    "Papad": df.iloc[row+5,col].replace('+', ''),
                    "Salad": df.iloc[row+6,col].replace('+', ''),
                    "Plain Rice": df.iloc[row+7,col].replace('+', ''),
                    "Extra": df.iloc[row+8,col].replace('+', '') 
            },meal_type_id=2,day_id=day+1))
            row = df[df.iloc[:, 0] == meal_types[2] ].index[0]
            session.add(Dish(dishes={
                "Snack": df.iloc[row,col].replace('+', ''),
                    "Tea and Coffee": df.iloc[row+1,col].replace('+', ''),
                    "Fruits": df.iloc[row+2,col].replace('+', '')
            },meal_type_id=3,day_id=day+1))
            row = df[df.iloc[:, 0] == meal_types[3] ].index[0]
            session.add(Dish(dishes={
                    "Dry Vegetable": df.iloc[row,col].replace('+', ''),
                    "Curry": df.iloc[row+1,col].replace('+', ''),
                    "Salad": df.iloc[row+2,col].replace('+', ''),
                    "Roti": df.iloc[row+3,col].replace('+', ''),
                    "Pickle": df.iloc[row+4,col].replace('+', ''),
                    "Plain Rice": df.iloc[row+5,col].replace('+', ''),
                    "Soup": df.iloc[row+6,col].replace('+', ''),
                    "Dessert": df.iloc[row+7,col].replace('+', ''),
                    "Milk": df.iloc[row+8,col].replace('+', ''),
                    "Extra": df.iloc[row+9,col].replace('+', '')
                },meal_type_id=4,day_id=day+1))
        session.commit()
        return {"status": "success"}

    except Exception as e:
        # Handle errors appropriately
        return {"status": "error"}

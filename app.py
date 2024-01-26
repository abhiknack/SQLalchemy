from fastapi import FastAPI, File, HTTPException, UploadFile
from checkInput import check_input
from create_table import create_table
from formFill import add_user
from insert_day_meal import insert_day_meal
from insert_menu import insert_menu
from retrive_comment import retrive_comment
from retrive_menu import get_menu
from insert_comment import insert_comment
from delete_table import delete_tables
app = FastAPI()

@app.get("/get-json")
def menu():
    json_data = get_menu()
    return json_data

@app.post("/insert-comment")
async def income_comment(json_data: dict):
    result = insert_comment(json_data)
    return result

@app.get("/delete-tables")
def delete_tab():
    result = delete_tables()
    return result

@app.get("/create-tables")
def create_tab():
    result = create_table()
    return result

@app.post("/insert-menu")
async def upload_excel(file: UploadFile = File(...)):
    return insert_menu(file)

@app.post("/retrive-comment")
async def retr_comment(json_data: dict):
    result = retrive_comment(json_data)
    return result

@app.get("/insert-day-meal")
def insert_days():
    result = insert_day_meal()
    return result

@app.post("/check-input")
async def input_check(json_data: dict):
    result = check_input(json_data)
    return result

@app.post("/add-user")
async def input_check(json_data: dict):
    result = add_user(json_data)
    return result

@app.post("/send-otp")
async def otp(json_data: dict):
    result = send_otp(json_data)
    return result
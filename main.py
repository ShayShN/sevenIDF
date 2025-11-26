from soldier import Soldier
from dorms import Bilding
from rooms import Rooms
from fastapi import FastAPI,File, UploadFile
import uvicorn
from datetime import datetime
import csv
import sqlite3


app = FastAPI()
data = []

connection = sqlite3.connect('db_shivata.db')
cursor = connection.cursor()
  
cursor.execute("""CREATE TABLE shivata (
personal_number INTEGER PRIMARY KEY,
first_name TEXT NOT NULL,
last_name TEXT NOT NULL,
gender TEXT NOT NULL,
city TEXT NOT NULL,
distance INTEGER,
placement_status BOOLEAN
)
""")
connection.commit()      
    
def func_sort(arr):
    return int(arr['distance']) 



@app.post("/assignWithCsv")
def get_file(file: UploadFile = File()):
    global data
    if not "csv" in file.content_type:
        return {"msg": f"content_type: `{file.content_type}` not allowed!"}
    text = file.file.read().decode()
   
    reader = csv.DictReader(text.splitlines())
    rows = [row for row in reader]
    columns = rows[0]
    rows = rows[1:]
 
    rows.sort(reverse=True, key=func_sort)
    data = rows
    for i in data:
        print(i)
    return rows[::]



def insert_soldier(soldier):
        cursor.execute('''INSERT INTO shivata(personal_number, first_name, last_name, gender, city, distance, placement_status)
                    VALUES(?,?,?,?,?,?,?)'''
                    , (soldier.personal_number, soldier.first_name, soldier.last_name, soldier.gender, soldier.city, soldier.distance, soldier.placement_status)
                    )
        connection.commit()

    
    
def add_soldier_to_room(arr_soldier):
    for i in arr_soldier:
        if len(Rooms.rooms) >= 8:
            Rooms.rooms.pop(i)
        else:
            x = i.pop(0)
            Rooms.rooms.append(x)
        
def add_to_dorms(rooms):
    if len(Bilding.dorm_a) >= 10 and len(Bilding.dorm_b) >= 10:
        return ("the 2 bildings is full!")
    elif len(Bilding.dorm_a) >= 10:
        Bilding.dorm_b.append(rooms)
    elif len(Bilding.dorm_b) >= 10:
        Bilding.dorm_a.append(rooms)

def check_km(arr):
    arr_new = []
    for i in arr:
        arr_new.append(arr[:80])
    return arr_new


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)


from typing import Self
from fastapi import FastAPI,File, UploadFile
import uvicorn
import csv
import sqlite3

app = FastAPI()




    

connection = sqlite3.connect('db_shivata.db')
cursor = connection.cursor()
        
# @app.get("/")
# def get_root():
#     return {"ts": datetime.now()}

@app.post("/assignWithCsv")
def get_file(file: UploadFile = File()):
    if not "csv" in file.content_type:
        return {"msg": f"content_type: `{file.content_type}` not allowed!"}
        
    text = file.file.read().decode()
    
        # Parse CSV
    reader = csv.reader(text.splitlines())
    rows = [row for row in reader]
    columns = rows[0]
    rows = rows[1:]
    cursor("drop table if exists shivata")
    cursor("""CREATE TABLE shivata (
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
        
    return rows
def insert_soldier(soldier):
        cursor.execute('''INSERT INTO shivata(personal_number, first_name, last_name, gender, city, distance, placement_status)
                    VALUES(?,?,?,?,?,?,?)'''
                    , (soldier.personal_number, soldier.first_name, soldier.last_name, soldier.gender, soldier.city, soldier.distance, soldier.placement_status)
                    )
        connection.commit()
def get_limit_80(arr_sol):
    rows = cursor.execute(
        'SELECT count(*), distance FROM shivata WHERE '
    )

if __name__ == "__main__":
    uvicorn.run(app)
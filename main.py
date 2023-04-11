from fastapi import FastAPI
import sqlite3
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
import json

# Підключення до бази даних
conn = sqlite3.connect(r"C:\Users\Sh1zik\Downloads\nomeroff-net-master\park_base.db")
cursor = conn.cursor()

# Запит на отримання даних
cursor.execute('SELECT * FROM cars')
data = cursor.fetchall()


# Створення fastapi додатку
app = FastAPI()
cars = {'cars':{}}
# Маршрут, який повертає дані у форматі json
@app.get('/data')
def get_data():
    data_list = []
    for user in data:
        user_data = {
            'name': user[1],
            'model': user[2],
            'number': user[3],
            'data_in': user[4],
            'data_out': user[5],
            'status': user[6]
        }
        data_list.append(user_data)
    cars['cars'] = data_list
    json_data = jsonable_encoder(cars)

    return JSONResponse(content=json_data)

# Запуск fastapi додатку
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8000)

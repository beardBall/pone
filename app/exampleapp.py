from typing import List, Dict
from flask import Flask
import mysql.connector
import json

app = Flask(__name__)
print("If you see me, it means the app is running #######")


config = {
'user': 'root',
'password': 'root',
'host': 'db',
'port': '3306',
'database': 'knights'
}

def favorite_colors() -> List[Dict]:
    
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM tasks')
    results = [{name: color} for (name, color) in cursor]
    cursor.close()
    connection.close()

    return results


def get_db() -> List[Dict]:
    sql = 'select * from tasks'
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    cursor.execute(sql)
    results = dict(cursor.fetchall())
    cursor.close()
    connection.close()
    return results



@app.route('/')
def index() -> str:
    # return json.dumps({'favorite_colors': favorite_colors()})
    return json.dumps({'tasks': getDB('SELECT * FROM tasks')})



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
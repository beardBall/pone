from typing import List, Dict
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


import mysql.connector
import json

app = Flask(__name__)
print("RUNNIGN appy.py ******")


# connection_str='mysql://root:root@localhost:336/knights'
# app.config['SQLALCHEMY_DATABASE_URI']=connection_str
# db = SQLAlchemy(app)


# class Todo(db.Model):
#      id = db.Column(db.Integer, primary_key=True)
#      content = db.Column(db.String(200), nullable=False)
#      completed = db.Column(db.Integer, default=0)
#      date_created = db.Column(db.DateTime, default=datetime.now)

#      def __repr__(self):
#           return '<task %r>' % self.id

config = {
    "user": "root",
    "password": "root",
    "host": "db",
    "port": "336",
    "database": "knights"
    }

# config = {
#     'user': 'root',
#     'password': 'root',
#     'host': 'db',
#     'port': '336',
#     'database': 'knights'
# }

def favorite_colors() -> List[Dict]:
   
    connection = mysql.connector.connect(config)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM favorite_colors')
    results = [{name: color} for (name, color) in cursor]
    cursor.close()
    connection.close()

    return results


def getDB(sql: str):
    config1 = {
    "user": "root",
    "password": "root",
    "host": "db",
    "port": "336",
    "database": "knights"
    }
    print(config1)
    connection = mysql.connector.connect(**config1)
    cursor = connection.cursor()
    cursor.execute(sql)
    results = dict(cursor.fetchall())
    cursor.close()
    connection.close()
    return results

# @app.route('/')
# def index() -> str:
#     return json.dumps({'favorite_colors': favorite_colors()})

@app.route('/')
def index() -> str:

    return json.dumps({'results': getDB('SELECT * FROM tasks')})


    # return json.dumps({'favorite_colors': Todo.query.all})


if __name__ == '__main__':
    # app.run(host='0.0.0.0')
    # with app.app_context():
    #     db.create_all()
    app.run(host='0.0.0.0', port=8000, debug=True)

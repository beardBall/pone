
import myconfig
from flask import Flask, render_template, request, redirect
import os, sys
import datetime
import json
import mysql.connector



app = Flask(__name__)
# print(__name__)
config = myconfig.config


def getData(sql):
    # print(myconfig.config['mysql'])
    # print('configg printed') 
    # sql = 'select * from tasks'
    # connection = mysql.connector.connect(
    #     host=myconfig.config['mysql']['host'],
    #     user=myconfig.config['mysql']['user'],
    #     password=myconfig.config['mysql']['password'],
    #     port=myconfig.config['mysql']['port'],
    #     database=myconfig.config['mysql']['database']
    #     )


    connection = mysql.connector.connect(
    **myconfig.config['mysql']
    )
    

    print(**myconfig.config['mysql'])


    cursor = connection.cursor(dictionary=True)
    cursor.execute(sql)

    results = cursor.fetchall()
    cursor.close()
    connection.close()
    return results

# print(myconfig.config['mysql'])
# sys.exit(os.EX_OK)

def insertData(sql):
    print(sql)
    connection = mysql.connector.connect(**myconfig.config['mysql'])
    cursor = connection.cursor()
    cursor.execute(sql)
    connection.commit()
    cursor.close()

    connection.close()


  

@app.route('/index.html', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def index():
    # getData()

    if request.method == 'POST':
        task_content = request.form['content']
        print(request.form)
        new_task = {'content': task_content, 'date_created': datetime.datetime.now()}
        try:
            #  insert_task(new_task)
            # with open("/data/one/" + task_content, "a") as f:
            #     f.write(task_content + "\n")
            # sql = f"INSERT INTO tasks (content, date_created) VALUES ('{task_content}', '{new_task['date_created']}')"
            sql = f"INSERT INTO tasks (content) VALUES ('{task_content}')"
            insertData(sql)
            return redirect('/')
        except Exception as e:
            return f'There was an issue adding your task: {str(e)}'

    else:
        tasks = getData('SELECT * FROM tasks')
        return render_template("index.html", tasks=tasks)



@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    if request.method == 'GET':
        # task_id = request.args.get('id')
        task_id = id

        if task_id:
            try:
                sql = f"DELETE FROM tasks WHERE id = {task_id}"
                insertData(sql)
                return redirect('/')
            except Exception as e:
                return f"Something bad happened: {str(e)}"
        else:
            return "No task ID provided"
    else:
        return "Invalid request method"


@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    if request.method =='POST':
        submitted_content = request.form['content']
        print(submitted_content)
        sql = f"UPDATE tasks SET content = '{submitted_content}' WHERE id = {id};"
        insertData(sql)
        return redirect('/')
    else:
        taskToUpdate = getData(f"Select * from tasks where id = {id};")  
        # print(taskToUpdate)
        return render_template('update.html', task=taskToUpdate)



 
@app.route('/disclaimer')
def disclaimer():
    return render_template('disclaimer.html', data=myconfig.config)



app.run(host='0.0.0.0', debug=True, port=80, threaded=True)








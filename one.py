from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

print("north")

with open("/data/one/first" , "a") as f:
      f.write("hello world" + "\n")



print(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////data/one/one.db'
db = SQLAlchemy(app)

class Todo(db.Model):
     id = db.Column(db.Integer, primary_key=True)
     content = db.Column(db.String(200), nullable=False)
     completed = db.Column(db.Integer, default=0)
     date_created = db.Column(db.DateTime, default=datetime.now)

     def __repr__(self):
          return '<task %r>' % self.id



@app.route('/', methods=['GET', 'POST'])
def index():
#     return "Hello world"
      if request.method == 'POST':
            task_content = request.form['content']
            new_task = Todo(content=task_content)
            try:
                  db.session.add(new_task)
                  db.session.commit()
                  with open("/data/one/" + task_content, "a") as f:
                        f.write(task_content + "\n")
                  return redirect('/')
            except:
                 return 'There was an issue adding your task'
      else:
            tasks = Todo.query.order_by(Todo.date_created).all()
            return render_template("index.html", tasks=tasks)


@app.route('/delete/<int:id>')
def delete(id):
      task_to_delete = Todo.query.get_or_404(id)
      print(task_to_delete)

      try:
           db.session.delete(task_to_delete)
           db.session.commit()
           return redirect('/')
      except:
            return "something bad happened"



@app.route('/update/<int:id>', methods=['GET','POST'])
def update(id):
      print("request.methods: " + str(request.method))

      taskToUpdate = Todo.query.get_or_404(id)
      if(request.method == 'POST'):
            taskToUpdate.content = request.form['content']
            
            #try to update database
            try:
                  db.session.commit()
                  return redirect('/')
            
            except:
                  return "will"




            return redirect('/')

      else:
            return render_template('update.html', task=taskToUpdate)


"""      try:
                        

            db.session.commit()

            return redirect('/')
      except:
            return "something bad happened"

"""




if __name__ == "__main__":
    with app.app_context():
         db.create_all()
    app.run(host="0.0.0.0", port=8000, debug=false)


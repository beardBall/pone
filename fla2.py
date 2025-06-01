import myconfig
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import datetime
import mython
from urllib.parse import urlparse



app = Flask(__name__)
print(__name__)
config = myconfig.config

# Configure SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = (
    f"mysql+mysqlconnector://{config['mysql']['user']}:{config['mysql']['password']}"
    f"@{config['mysql']['host']}:{config['mysql']['port']}/{config['mysql']['database']}"
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define Task model
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    date_updated = db.Column(db.DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

    def __repr__(self):
        return f'<Task {self.id}>'

# Create tables (run once, or use Flask-Migrate for production)
with app.app_context():
    db.create_all()

@app.route('/index.html', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def index():
    urll = {}
    print(request.base_url)
    urlbits =urlparse(request.url).netloc
    urll['full_url'] =  request.url 
    urll['protocol'] =  urll['full_url'].split(':')[0] 
    urll['domain']  = urll['full_url'].split(':')[1].lstrip('/')
    urll['page'] = urll['full_url'].split('/')[-1]

    try:
        urll['params'] = urll['full_url'].split('?')[1]
    # except IndexError:
    except Exception as e:
        print("no params provided: " + str(e))
    else:
        print("this is executed if no exceptions occurred.")


    # domain = urlparse(request.base_url.netloc)
    # directory = urlparse(request.base_url)


    print(urll)
    if request.method == 'POST':
        task_content = request.form['content']
        try:
            new_task = Task(content=task_content)
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except Exception as e:
            return f'There was an issue adding your task: {str(e)}'
    else:
        tasks = Task.query.order_by(Task.date_created.asc()).all()
        return render_template("index.html", tasks=tasks)

@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    task = Task.query.get_or_404(id)
    try:
        db.session.delete(task)
        db.session.commit()
        return redirect('/')
    except Exception as e:
        return f"Something bad happened: {str(e)}"

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    task = Task.query.get_or_404(id)
    if request.method == 'POST':
        task.content = request.form['content']
        db.session.commit()
        return redirect('/')
    else:
        return render_template('update.html', task=task)

@app.route('/disclaimer')
def disclaimer():
    return render_template('disclaimer.html', data=myconfig.config)

app.run(host='0.0.0.0', debug=True, port=81, threaded=True)
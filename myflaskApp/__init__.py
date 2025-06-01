from flask import Flask 
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for



app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
@app.route('/index.html', methods=['GET', 'POST'])
def index():

    return render_template('index.html')


@app.route('/add', methods=['GET', 'POST'])
def add():
    pass 


@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete():
    pass


@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    pass



def appStart(config):
    print(config['hosting'])
    # app.run(host=config['hosting']['host'], port=config['hosting']['port'], debug=True)
    app.run(**config['hosting'])

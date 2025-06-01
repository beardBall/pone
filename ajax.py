from flask import Flask, request, jsonify, render_template
from time import time
import json

app = Flask(__name__)
@app.route('/', methods=['POST', 'GET'])
def index():
    seconds = time()
    if request.is_json:
        if request.method =='GET':
            text = request.args.get('button_text')
            print(f"text: {text}")
            # data = request.get_json()
            return jsonify({"seconds": seconds})
                           
        if request.method =='POST':
            print(request.data)
            card_text = json.loads(request.data).get('text')
            new_text = f'I got {card_text}'
            return jsonify({"data": new_text})


            
    else: 
        datatosend = {'seconds': seconds}
        return render_template('main.html', data=datatosend)
    


app.run(debug=True, host='0.0.0.0', port=50)

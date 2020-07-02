from flask import Flask,render_template, request
import pickle
import math
from mdl_pkld import model


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/result', methods=['post'])
def predict():
    x = int(request.form['x'])
    y = int(request.form['y'])
    z = int(request.form['z'])
    ip = model([x,y,z])[0]
    return render_template('result.html', pred_out = math.ceil(ip))
    

if __name__ == "__main__":
    app.run(debug=True)
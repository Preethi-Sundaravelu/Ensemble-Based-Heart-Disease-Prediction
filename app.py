from ast import parse
from urllib import response
import numpy as np
from flask import Flask, render_template, request
import pickle
import requests
import json
from datetime import date, datetime



app = Flask(__name__)

model = pickle.load(open('RandomForest.pkl', 'rb'))
@app.route('/index2',methods=['GET','POST'])
def index2():
    return render_template('index2.html')
def index():
    return render_template('index.html')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():

    # age = request.form['age']
    # cpt=request.form['cpt']
    # rbp=request.form['rbp']
    # chl=request.form['chl']
    # mhr=request.form['mhr']
    # eia=request.form['eia']
    # opk=request.form['opk']
    # slp=request.form['slp']
    # ca=request.form['ca']
    # tha=request.form['tha']

    age = float(request.form['age'])
    cpt = float(request.form['cpt'])
    rbp = float(request.form['rbp'])
    chl = float(request.form['chl'])
    mhr = float(request.form['mhr'])
    eia = float(request.form['eia'])
    opk = float(request.form['opk'])
    slp = float(request.form['slp'])
    ca = float(request.form['ca'])
    tha = float(request.form['tha'])
       
    
    output = "No output"

    data = np.array([[age,cpt,rbp,chl,mhr,eia,opk,slp,ca,tha]])
    print("entered")
    pr=np.array([[68.0,	4.0,	144.0	,193.000000,	141.0,	0.0	,3.4,	2.000000,	2.000000,	7.000000]])
    prediction = model.predict(data)
    if(prediction==0):
        output= "No heart disease diagnosed!!"
    else:
        output="Sorry! We regret to inform that you have been diagnosed with heart disease! "

    return render_template('index.html', prediction_text=output)

if __name__ == "__main__":
    app.run()

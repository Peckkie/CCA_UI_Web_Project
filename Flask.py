from flask import Flask, render_template, request
import requests 
import json
import pandas as pd
import sys 

app = Flask(__name__)

@app.route("/nav", methods =['POST','GET'])  

def home():
  
  if request.method =='POST':
    dbtb = pd.read_csv('db.csv')
    user_ID = '1101'
    user_sequence	= 1
    unique_ID	= '1101'
    element_1	= request.form.get("fname")
    element_2	= request.form.get("fname")
    element_3	= request.form.get("fname")
    element_4	= request.form.get("fname")
    element_5 = request.form.get("fname")

    dbtb = dbtb.append({'User_ID':user_ID,	'User_Sequence':user_sequence,	'Unique_ID':unique_ID,
    'Element_1':element_1,	'Element_2':element_2,	'Element_3':element_3,	'Element_4':element_4,'Element_5':element_5}, ignore_index=True)
    dbtb.to_csv('db.csv', index=False)
    return render_template("nav-active.html")

  return render_template("nav-click.html")

@app.route("/click", methods =['POST','GET'])  
def home2():
  
  if request.method =='POST':
    dbtb = pd.read_csv('db.csv')
    user_ID = '2201'
    user_sequence	= 4
    unique_ID	= '2201'
    element = request.form.get("element")
    x = element.split(",")
    element_1	= x[0]
    element_2	= x[1]
    element_3	= x[2]
    element_4	= x[3]
    element_5 = x[4]

    dbtb = dbtb.append({'User_ID':user_ID,	'User_Sequence':user_sequence,	'Unique_ID':unique_ID,
    'Element_1':element_1,	'Element_2':element_2,	'Element_3':element_3,	'Element_4':element_4,'Element_5':element_5}, ignore_index=True)
    dbtb.to_csv('db.csv', index=False)
    return render_template("nav-active.html")

  return render_template("nav-click.html")



if __name__ == "__main__":
    app.run()
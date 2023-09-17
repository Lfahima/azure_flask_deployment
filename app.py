from flask import Flask, render_template
import pandas as pd
import random


app = Flask(__name__)

@app.route('/')
def mainpage():
    return render_template('base.html', name = "Fahima")

@app.route('/about')
def aboutpage():
    return render_template('about.html')

@app.route('/random')
def randomnumber():
    number_var = random.randint(1, 10000)
    return render_template('random.html', single_number = number_var)


df = pd.read_csv('./data/Healthcare-Diabetes.csv')
@app.route('/data')
def data(data=df):
    data = data.sample(15)
    return render_template('data.html', data=data)

if __name__ == '__main__':
    app.run(
        debug=True,
        port=8080
    )
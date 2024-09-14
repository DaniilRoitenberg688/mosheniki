import random
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    # TODO: добавить в форму поля ИМЯ, дата, CVC
    return render_template('index.html')

@app.route('/save', methods=['POST'])
def save():
    number = request.form['number']
    name = request.form['name']
    date = request.form['date']
    cvc = request.form['cvc']

    if len(number) != 16 or not number.isdigit():
        return render_template('index.html', message="что-то не так с номером карты")

    if '/' not in date:
        return render_template('index.html', message="что-то не так с датой карты")


    return render_template('result.html', role=random.choice(['вупсень', "пупсень"]))

# запускаем сайт
app.run(debug=True)
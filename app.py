from flask import Flask, render_template, request, redirect, flash
from forex_python.converter import RatesNotAvailableError, DecimalFloatMismatchError
from refactor import convert

app = Flask(__name__)

app.config['SECRET_KEY'] = 'ForexConverter'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/result', methods=['POST'])
def result():
    # convertFrom = request.args['convertFrom'].upper()
    # convertTo = request.args['convertTo'].upper()
    # amount = float(request.args['amount'])
    convertFrom = request.form['convertFrom'].upper()
    convertTo = request.form['convertTo'].upper()
    amount = float(request.form['amount'])
    try:
        result = convert(convertFrom, convertTo, amount)
        # Exception is an instance of class
    except RatesNotAvailableError:
        flash(f'Not a valid conversion: {convertFrom} => {convertTo}.')
        return redirect('/')
    except DecimalFloatMismatchError:
        flash(f'Not a valid amount: {amount}.')
        return redirect('/')
    return render_template('result.html', convertFrom=convertFrom, convertTo=convertTo, amount=amount, result=result)

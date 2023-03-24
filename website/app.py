from flask import Flask, redirect, render_template, url_for, request
from logic import find_food

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('home.html')

@app.route('/input', methods= ['POST','GET'])
def input():
    if request.method == 'POST':
        ingredient = request.form["nm"]
        return redirect(url_for('food', result = ingredient))
    else:
        return render_template('ingredient.html')

@app.route('/<result>')
def food(result):
    final = find_food(result)
    return final


if __name__ == '__main__':
    app.run()
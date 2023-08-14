from flask import Flask, render_template, redirect,url_for

from db import add_user

app = Flask(__name__)


@app.route('/')
def login():
    return render_template('index.html')
    return redirect(url_for('portfolio'))


@app.route('/portfolio', methods=['GET'])
def portfolio():
    return render_template('portfolio.html')

if __name__ == "__main__":
    app.run(debug=True)
    add_user()
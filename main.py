from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


# Это страница сайта#
@app.route('/about')
def about():
    return render_template('about.html')


# Заменить True на False при выгрузке на сервер#
if __name__ == '__main__':
    app.run(debug=True)

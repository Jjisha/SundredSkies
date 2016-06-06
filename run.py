from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def start():
    title = 'Startseite'
    return render_template('index.html', title=title)


@app.route('/fertigkeiten')
def fertigkeiten():
    return render_template('fertigkeiten.html')


if __name__ == '__main__':
    app.run(debug=True)

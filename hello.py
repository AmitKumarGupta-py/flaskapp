from flask import Flask

app = Flask(__name__)

@app.route('/')

def hello():
    return "Its Lunch Time.. empty stomach does not digest anything... especially study!!!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello Welcome to My Flask App"

@app.route('/about')
def about():
    return "This app is created using Flask"

if __name__ == '__main__':
    app.run(debug=True)
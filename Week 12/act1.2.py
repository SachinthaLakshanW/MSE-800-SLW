from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_flask():
    return "<h1>Hello, Flask</h1>"

@app.route("/bye")
def hello_bye():
    return "<h1>Bye, Flask</h1>"

@app.route("/username/<name>")
def hello_user_name(name):
    return f"<h1>{name} is learning Flask</h1>"

@app.route("/cal/<int:number>")
def show_square(number):
    return f"<h1>The square of {number} is {number**2}</h1>"

if __name__ == "__main__":
    app.run(debug=True)

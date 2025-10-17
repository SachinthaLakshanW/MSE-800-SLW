from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_flask():
    return "<h1>Hello, Flask</h1>"

@app.route("/bye")
def hello_Bye():
    return "<h1>Bye, Flask</h1>"

if __name__ == "__main__":
    app.run(debug=True)

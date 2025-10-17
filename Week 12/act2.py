from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return '''
        <h1>Activity Flask Image Loader</h1>
        <a href="/">Home</a>
        <form action="/show_image" method="post">
            <p>Enter Image URL:</p>
            <input type="text" name="image_url" placeholder="Paste image link here" size="50">
            <input type="submit" value="Load">
        </form>
    '''

@app.route("/show_image", methods=["POST"])
def show_image():
    image_url = request.form["image_url"]
    return f'''
        <h1>Image Preview</h1>
        <a href="/">Back</a><br><br>
        <img src="{image_url}" width="400">
    '''

if __name__ == "__main__":
    app.run(debug=True)

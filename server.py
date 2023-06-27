from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/',methods=["POST","GET"])
def index():
    if request.method == "POST":
        name = request.form['name']
        return name
    return render_template('index.html')

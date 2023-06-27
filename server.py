from flask import Flask, redirect, render_template, request, session
app = Flask(__name__)
app.config['SECRET_KEY'] = 'Temporary'

@app.route('/',methods=["POST","GET"])
def index():
    if request.method == "POST":
        name = request.form['name']
        session['name'] = name
        return redirect('/quiz')
    return render_template('index.html')

@app.route('/quiz',methods=["POST","GET"])
def quiz():
    name = session.pop('name',None)
    if request.method == "POST":
        pass
    return render_template('quiz.html',name=name)

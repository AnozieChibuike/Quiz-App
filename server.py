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

quiz_data = {
    'questions': [
        {
            'question': 'What is the resitivity of a cylindrical material wire whose 1m length has a resistance of 2ohms? The diameter of a wire is 0.5m',
            'options': ['3.97 x 10⁻⁷','3.93 x 10⁻⁷','3.93 x 10⁻⁶','3.93'],
            'answer': '3.93 x 10⁻⁷',
        },
        {
            'question': 'Find the resistance of a wire of length 0.64m,radius 0.2mm and resistivity 3 x 10-6 ',
            'options': ['15 ohms','15.5 ohms','1.5 ohms','50 ohms'],
            'answer': '15.5 ohms',
        },
        {
            'question': 'According to ohm’s law, the ratio V/I is constant for',
            'options': ['an electrolyte', 'a diode', 'transistor', 'silver'],
            'answer': 'silver',
        },
        {
            'question': 'Which of the following is NOT an effect​ that can be produced by an electric current',
            'options': ['Heat', 'Light', 'Sound', 'None of these'],
            'answer': 'None of these',
        },
        {
            'question': 'The total energy required to send a unit positive charge round a complete electrical circuit is the',
            'options': ['Kinetic energy', 'Potential difference', 'Electromotive force', 'Electrical energy'],
            'answer': 'Electromotive force',               
        },
    ]
}
        
            





@app.route('/quiz',methods=["POST","GET"])
def quiz():
    name = session['name']
    if request.method == "POST":
        li = []
        score = 0
        quest = 0
        for key, value in request.form.items():
            li.append(value)
            quest += 1
        for i, question in enumerate(quiz_data['questions']):
            select = li[i]
            correct = question['answer']
            if select == correct:
                score += 1
        return render_template('result.html',name=name,score=score,total_questions=quest)
        
    return render_template('quiz.html',name=name,quiz_data=quiz_data)

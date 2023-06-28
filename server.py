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
        {
            'question': 'Which of the following obey ohm’s law ?',
            'options': ['Glass','Diode', 'All electrolytes', 'All metals'],
            'answer': 'All metals',
        },
        {
            'question': 'When a charge moves through an electric circuit in the direction of an electric force',
            'options': ['gains both potential and kinetic energy.', 'gains potential energy and loses kinetic energy', 'Loses potential energy and gains kinetic energy', 'Loses both potential and kinetic energy'],
            'answer': 'Loses potential energy and gains kinetic energy',
        },
        {
            'question': 'An electric cell has an internal resistance of 2ohms. A current of 0.5A is found to flow when a resistor of 5ohms resistance is connected across it . What is the electromotive force of the cell ?',
            'options': ['5 volts', '3.5 volts', '2.5 volts', '10 volts'],
            'answer': '10 volts',
        },
        {
            'question': 'All of these obey ohms law except',
            'options': ['Transistor', 'Resistors', 'Rectifiers', 'Insulators'],
            'answer': 'Insulators',
        },
        {
            'question': 'The unit of current is',
            'options': ['Ampere','Volts','Ohms','Joules'],
            'answer': 'Ampere',
        },
        {
            'question': 'The opposition to the flow of charges (electrons) or current is',
            'options': ['Insulator', 'Resistance', 'Ammeter', 'Emf'],
            'answer': 'Resistance',
        },
        {
            'question': 'The unit of resistance is',
            'options': ['Ohms', 'Ampere', 'Volts', 'Current'],
            'answer': 'Ohms',
        },
        {
            'question': 'The pd between the terminals of a cell when it is not delivering any current in an external circuit (or when it is in an open circuit)',
            'options': ['Resistance', 'Emf', 'Electricity', 'Potential difference'],
            'answer': 'Emf',
        },
        {
            'question': 'The unit of potential difference is',
            'options': ['Volt', 'Ampere', 'Coulomb', 'Ohms'],
            'answer': 'Volt',
        },
        {
            'question': 'The formation of hydrogen gas bubbles around the copper plate of the simple cell is ',
            'options': ['Depolarization', 'Polarization', 'Local action', 'Electrolyte'],
            'answer': 'Polarization',
        },
        {
            'question': 'Polarization of cells can be reduced or prevented by adding',
            'options': ['Sulphur oxide', 'Carbon (IV) oxide', 'Manganese di oxide', 'Helium'],
            'answer': 'Manganese di oxide',
        },
        {
            'question': 'Local action can be prevented by the process of',
            'options': ['Polarization', 'Depolarization', 'Amalgamation', 'Electricity'],
            'answer': 'Amalgamation',
        },
        {
            'question': 'What is caused due to impurities in the zinc plate \n A. Polarization ',
            'options': ['Polarization', 'Thermometer', 'Local action', 'Amalgamation'],
            'answer': 'Local action',
        },
        {
            'question': 'A cell of emf of 2V and internal resistance 1ohm supplies a current of 0.5A to a resistance whose value is ',
            'options': ['0.5W', '1W', '2.5W', '3W'],
            'answer': '3W',
        },
        {
            'question': 'A 24V potential difference is applied across a parallel combination of four 6 ohm resistors. The current in each resistor is',
            'options': ['1A', '4A', '16A', '18A'],
            'answer': '4A',
        }
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

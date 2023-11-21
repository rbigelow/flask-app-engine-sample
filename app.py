from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return 'Hello, world!'

@app.route('/name', methods=['GET'])
def name():
    name = 'Ross'
    return 'my name is ' + name 

@app.route('/colleges', methods=['GET'])
def colleges():
    colleges = [ 
        {'name': 'Algonquin College', 'location': 'Ottawa'},
        {'name': 'Cambrian College', 'location': 'Sudbury'},
        {'name': 'Canadore College', 'location': 'North Bay'},
        {'name': 'Centennial College', 'location': 'Toronto'},
        {'name': 'Conestoga College', 'location': 'Kitchener'},
        {'name': 'Confederation College', 'location': 'Thunder Bay'},
        {'name': 'Durham College', 'location': 'Oshawa'},
        {'name': 'Fanshawe College', 'location': 'London'},
        {'name': 'Fleming College', 'location': 'Peterborough'},
        {'name': 'George Brown College', 'location': 'Toronto'},
        {'name': 'Georgian College', 'location': 'Barrie'},
        {'name': 'Humber College', 'location': 'Toronto'},
        {'name': 'La Cite Collegiale', 'location': 'Ottawa'},
        {'name': 'Lambton College', 'location': 'Sarnia'},
        {'name': 'Loyalist College', 'location': 'Belleville'},
        {'name': 'Mohawk College', 'location': 'Hamilton'},
        {'name': 'Niagara College', 'location': 'Welland'},
        {'name': 'Northern College', 'location': 'Timmins'},
        {'name': 'St. Clair College', 'location': 'Windsor'},
        {'name': 'St. Lawrence College', 'location': 'Kingston'},
        {'name': 'Sault College', 'location': 'Sault Ste. Marie'},
        {'name': 'Seneca College', 'location': 'Toronto'},
        {'name': 'Sheridan College', 'location': 'Oakville'},
        {'name': 'Sir Sandford Fleming College', 'location': 'Peterborough'},
        {'name': 'St. Clair College', 'location': 'Windsor'},
        {'name': 'St. Lawrence College', 'location': 'Kingston'},
        {'name': 'Sault College', 'location': 'Sault Ste. Marie'},
        {'name': 'Seneca College', 'location': 'Toronto'},
        {'name': 'Sheridan College', 'location': 'Oakville'},
        {'name': 'Sir Sandford Fleming College', 'location': 'Peterborough'},
        {'name': 'St. Clair College', 'location': 'Windsor'},
    ]
    return colleges

@app.route('/enrolment', methods=['GET'])
def enrolment():
    name = 'Ross'
    return render_template('enrolment.html', name=name)

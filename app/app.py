import flask
from flask import request, jsonify
app = flask.Flask(__name__)
app.config["DEBUG"] = True
#from utils import *

# Create some test data for our catalog in the form of a list of dictionaries.


flight = [
    {
        "id": 1,
        "isbn":"9781593279509",
        "title":"Eloquent JavaScript, Third Edition",
        "subtitle":"A Modern Introduction to Programming",
        "author":"Marijn Haverbeke",
        "published":"2018-12-04T00:00:00.000Z",
        "publisher":"No Starch Press",
        "pages":472,
        "description":"JavaScript lies at the heart of almost every modern web application, from social apps like Twitter to browser-based game frameworks like Phaser and Babylon. Though simple for beginners to pick up and play with, JavaScript is a flexible, complex language that you can use to build full-scale applications.",
        "website":"http://eloquentjavascript.net/"
    },
    {
        "id": 2,
        "isbn":"9781491943533",
        "title":"Practical Modern JavaScript",
        "subtitle":"Dive into ES6 and the Future of JavaScript",
        "author":"Nicolás Bevacqua",
        "published":"2017-07-16T00:00:00.000Z",
        "publisher":"O'Reilly Media",
        "pages":334,
        "description":"To get the most out of modern JavaScript, you need learn the latest features of its parent specification, ECMAScript 6 (ES6). This flight provides a highly practical look at ES6, without getting lost in the specification or its implementation details.",
        "website":"https://github.com/mjavascript/practical-modern-javascript"
    }
]




@app.route('/', methods=['GET'])
def home():
    return '''<h1>smart flights</h1> <p>A flask api </p>'''

@app.route('/api/v1/flight/all', methods=['GET'])
def api_all():
    criterias = ''
    flights  = get_flight(criterias)
    return jsonify('flights')
    
@app.route('/api/v1/flight', methods=['GET'])
def api_id():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."
    results = []
    
    for flight in flight:
        if flight['id'] == id:
            results.append(flight)
            return jsonify(results)

@app.route("/api/v1/flight",  methods = ['POST'])
def api_insert():
    flight = request.get_json()
    flight.append(flight)
    return "Success: flight information has been added."


@app.route("/api/v1/flight/<id>", methods=["DELETE"])
def api_delete(id):
    for flight in flight:
        if flight['id'] == int(id):
            flight.remove(flight)
    return "Success: flight information has been deleted."



def get_flight(criteria):
    # connect to api 
    flight_list = get_flight_from_proveedor(criteria)
    origin_distination = process_flights(flight_list)

    return origin_distination

def get_flight_from_proveedor(criteria):
    
    
    return criteria

def process_flights(criteria):

    return criteria



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)

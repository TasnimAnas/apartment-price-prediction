from flask import Flask, jsonify, request
from flask_cors import CORS

import util

app = Flask(__name__)
CORS(app)


@app.route('/')
def Hello():
    return "Hello World"


@app.route('/get_location')
def get_location():
    response = jsonify({
        'locations': util.get_location_names()
    })
    return response


@app.route('/get_price', methods=['POST'])
def get_price():
    location = request.form['location']
    sqft = float(request.form['sqft'])
    bath = int(request.form['bath'])
    balcony = int(request.form['balcony'])
    bhk = int(request.form['bhk'])
    # return request.form
    print(location, sqft, bath, balcony, bhk)
    response = jsonify({
        'price': util.estimated_price(location=location, sqft=sqft, bath=bath, balcony=balcony, bhk=bhk)
    })
    return response


if __name__ == "__main__":
    print("Python server started")
    util.get_saved_artifacts()
    app.run()

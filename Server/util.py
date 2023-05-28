import json
import pickle

import numpy as np

__locations = None
__model = None
__data_columns = None


def estimated_price(location, sqft, bath, balcony, bhk):
    x = np.zeros(len(__data_columns))
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1
    x[0] = sqft
    x[1] = bath
    x[2] = balcony
    x[3] = bhk
    if loc_index >= 0:
        x[loc_index] = 1
    return round(__model.predict([x])[0], 2)


def get_location_names():
    return __locations


def get_saved_artifacts():
    print("Getting saved artifacts")
    global __locations
    global __data_columns
    global __model
    with open('./artifacts/columns.json', 'r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[4:]
    with open('./artifacts/banglore_home_prices_model.pickle', 'rb') as f:
        __model = pickle.load(f)
    print("Artifact loading is complete")

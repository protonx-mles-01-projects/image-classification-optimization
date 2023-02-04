from detector import detector_blueprint
from flask import request
import os
from app import app
import numpy as np


@detector_blueprint.route('/api/detect', method=['POST'])
def detect():
    # TODO: write detect image api
    input_data = request.get_json()
    # Convert the input data to a numpy array
    input_data = np.array(input_data)
    print(input_data.shape)
    return f'Image has shape {input_data.shape}'

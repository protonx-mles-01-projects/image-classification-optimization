from detector import detector_blueprint
from flask import request
import os
from app import app
import numpy as np
from flask import jsonify
import cv2

@detector_blueprint.route('api/detect', method=['POST'])
def detect():
    # TODO: write detect image api
    if request.files:
        binary_files = request.files.get('image_file').read()
        img = cv2.imread(binary_files)
        return f"Image has shape {img.shape}"
    
    return jsonify({
        "message": "Don't have image to detect",
        "status": False
    })

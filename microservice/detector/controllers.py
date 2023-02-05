import cv2
import numpy as np
from flask import jsonify, request
from detector import detector_blueprint

@detector_blueprint.route('/api/detect', methods=['POST'])
def detect():
    # TODO: write detect image api
    if request.files:
        binary_files = request.files.get('image_file').read()
        img = cv2.imdecode(np.frombuffer(binary_files, np.uint8), -1)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        return f"Image has shape {img.shape}"
    
    return jsonify({
        "message": "Don't have image to detect",
        "status": False
    })

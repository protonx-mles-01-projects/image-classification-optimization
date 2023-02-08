import onnxruntime as ort
from flask import jsonify, request
from detector import detector_blueprint
from common import preprocess_image

MODEL_PATH = "model_onnx/model.onnx"

# Load model
sess = ort.InferenceSession(MODEL_PATH)
input_name = sess.get_inputs()[0].name
label_name = sess.get_outputs()[0].name

@detector_blueprint.route('/api/detect', methods=['POST'])
def detect():
    # TODO: write detect image api
    if request.files:
        binary_files = request.files.get('image_file').read()
        img = preprocess_image(binary_files)
        predict = sess.run([label_name], {input_name: img})
        result = 'cat' if(predict[0] == 0) else 'dog'
        return jsonify({
            "message": "Successfully",
            "result": result
        })
    
    return jsonify({
        "message": "Failed",
        "reason": "Don't have image to detect",
    })

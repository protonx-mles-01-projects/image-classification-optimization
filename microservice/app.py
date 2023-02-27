import json
from flask import Flask, jsonify
from detector.controllers import detector_blueprint

# TODO: Init app
app = Flask(__name__)

try:
    with open('config/app-config.json', 'r') as f:
        config = json.load(f)
        config['debug'] = True if config['debug'] else False
        config['use_reloader'] = True if config['use_reloader'] else False
except:
    config = {
        'host': 'localhost',
        'port': 3000
    }

# TODO: register blueprint
app.register_blueprint(detector_blueprint)


@app.route('/', methods=['GET'])
def default_api():
    return jsonify({
        "message": "This is default api"
    })


# TODO: Start app
if __name__ == '__main__':
    app.run(**config)

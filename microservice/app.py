from flask import Flask
from detector import detector_blueprint
import json

#TODO: Init app
app = Flask(__name__)

#TODO: register blueprint
app.register_blueprint(detector_blueprint)

with open('config/app-config.json', 'r') as f:
    config = json.load(f)
    
#TODO: Start app
if __name__ == '__main__':
    app.run(**config)
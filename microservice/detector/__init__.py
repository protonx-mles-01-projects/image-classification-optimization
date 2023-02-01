"""
Init detect blueprint
"""
from flask import Blueprint

detector_blueprint = Blueprint(
    'detector',
    __name__,
    url_prefix=''
)
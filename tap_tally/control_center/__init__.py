from flask import Blueprint

control_center = Blueprint('control_center', __name__)

from . import views

from . import control_center


@control_center.route('/')
def hello():
    return "Hello"

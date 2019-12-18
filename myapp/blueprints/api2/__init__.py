from flask import Blueprint
from myapp.blueprints.api2.views import ApiTwo

api_two = Blueprint('api_two', __name__, url_prefix='/api_two')
api_two_view = ApiTwo.as_view('api_two')
api_two.add_url_rule('/<int:id>', view_func=api_two_view, methods=['GET',])

def init_app(app):
    app.register_blueprint(api_two)
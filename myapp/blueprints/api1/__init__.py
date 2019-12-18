from flask import Blueprint
from myapp.blueprints.api1.views import ApiOne, verify_count, verify_requests

api_one = Blueprint('api_one', __name__, url_prefix='/api_one')
api_one_view = ApiOne.as_view('api_one')
api_one.add_url_rule('/clientes', defaults={'id': None}, view_func=api_one_view, methods=['GET',])
api_one.add_url_rule('/clientes', view_func=api_one_view, methods=['POST',])
api_one.add_url_rule('/clientes/<int:id>', view_func=api_one_view, methods=['GET', 'PUT', 'DELETE'])
api_one.add_url_rule('/verifycount/<int:id>', view_func=verify_requests)
api_one.before_request(verify_count)

def init_app(app):
    app.register_blueprint(api_one)
        
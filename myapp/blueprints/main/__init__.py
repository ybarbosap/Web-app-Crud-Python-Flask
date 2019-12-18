from flask import Blueprint
from myapp.blueprints.main.views import (
    index, create, update_cliente, dell_cliente
)

main = Blueprint('main', __name__)
main.add_url_rule('/', view_func=index, methods=['GET', 'POST'])
main.add_url_rule('/create', view_func=create, methods=('POST',))
main.add_url_rule('/<int:id>/update', view_func=update_cliente, methods=['POST',])
main.add_url_rule('/<int:id>/dell', view_func=dell_cliente)

def init_app(app):
    app.register_blueprint(main)
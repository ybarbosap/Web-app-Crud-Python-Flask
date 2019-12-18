from flask import request, jsonify
from flask.views import MethodView
from myapp.models import Cliente, Count

class ApiTwo(MethodView):
    def get(self, id):
        try:
            cliente = Cliente.query.filter_by(id=id).first()
            count = Count.query.first()
            resp = {
                'Cliente': cliente.name,
                'Preço a pagar': count.count_request * cliente.valor
            }
            return jsonify(resp), 200
        except AttributeError:
            return jsonify({'message': 'Cliente não encontrado'}), 404

    def put(self):
        pass

    def delete(self):
        pass

    def post(self):
        pass


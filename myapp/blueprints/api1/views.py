from flask import jsonify, request
from flask.views import MethodView
from myapp.models import Cliente, Count
from myapp.ext.database import db

from sqlalchemy.orm.exc import UnmappedInstanceError

class ApiOne(MethodView):

    def get(self, id):
        if id is None:
            clientes = Cliente.query.all()
            return jsonify({'clientes': [cliente.to_json() for cliente in clientes]}), 200
        else:
            cliente = Cliente.query.filter_by(id=id).first()
            try:
                return jsonify(cliente.to_json()), 200
            except AttributeError:
                return jsonify({'message': 'Cliente não encontrado'}), 404  

    def post(self):
        data = request.get_json()
        c = Cliente(name=data['name'], valor=data['valor'])
        db.session.add(c)
        db.session.commit()
        return jsonify(c.to_json()), 201
    
    def delete(self, id):
        c = Cliente.query.filter_by(id=id).first()
        try:
            db.session.delete(c)
            db.session.commit()
        except UnmappedInstanceError:
            return jsonify({'message': 'Cliente não encontrado'}), 404
        return jsonify({'message': 'deleted'})
    
    def put(self, id):
        c = Cliente.query.filter_by(id=id).first()
        try:
            data = request.get_json()
            c.name = data['name']
            c.valor = data['valor']
            db.session.add(c)
            db.session.commit()
        except AttributeError:
            return jsonify({'message': 'Cliente não encontrado'}), 404
        return jsonify(c.to_json()), 200


def verify_requests(id):
    count = Count.query.first()
    if count is None:
        return jsonify({'message':'count não encontrado'})

    cliente = Cliente.query.filter_by(id=id).first()
    if cliente is None:
        return jsonify({'message':'cliente não encontrado'})
    
    response = {
        'cliente':cliente.name,
        'total_count_requests':count.count_request
    }
    return jsonify(response), 200


def verify_count():
    count = Count.query.first()
    if count is None:
        count = Count(count_request=1)
        
    count.count_request = count.count_request + 1
    db.session.add(count)
    db.session.commit()
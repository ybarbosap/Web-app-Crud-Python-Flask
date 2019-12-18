from myapp.ext.database import db

class Cliente(db.Model):
    __tablename__ = 'clientes'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(64))
    valor = db.Column(db.Float())

    def to_json(self):
        clientes_json = {
            'id': self.id,
            'name': self.name,
            'valor': self.valor
        }
        return clientes_json


class Count(db.Model):
    __tablename__ = 'counts'
    id = db.Column(db.Integer(), primary_key=True)
    count_request = db.Column(db.Integer())



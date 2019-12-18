import json, requests
from flask import render_template, redirect, url_for, request
from myapp.models import Cliente, Count
from myapp.ext.database import db


def index():
    clientes = Cliente.query.all()
    
    listCliente = []
    for cliente in clientes:
        new = [cliente.id, cliente.name, cliente.valor, calc_pagamento(cliente.id)] 
        listCliente.append(new)
    
    return render_template('index.html', clientes=listCliente, count=check())


def create():
    if request.method == 'POST':
        name = request.form['nome']
        valor = request.form['valor']
        c = Cliente(name=name, valor=valor)
        db.session.add(c)
        db.session.commit()
    return redirect(url_for('main.index'))
        

def dell_cliente(id):
    try:
        c = Cliente.query.filter_by(id=id).first()
        db.session.delete(c)
        db.session.commit()
        return redirect(url_for('main.index'))
    except:
        pass
    
    return redirect(url_for('main.index'))


def update_cliente(id):
    if request.method == 'POST':
        name = request.form['nome']
        valor = request.form['valor']
        try:
            c = Cliente.query.filter_by(id=id).first()
            c.name = name
            c.valor = valor
            db.session.add(c)
            db.session.commit()
            return redirect(url_for('main.index'))
        except:
            pass
    
    c = Cliente.query.filter_by(id=id).first()

    return redirect(url_for('main.index'))


def check():
    try:
        count = Count.query.first()
    except:
        count = None
    return count.count_request


def calc_pagamento(id):
    page_response = requests.get(f'http://127.0.0.1:5000/api_two/{id}')
    response = json.loads(page_response.text)
    return response['Preço a pagar']
    
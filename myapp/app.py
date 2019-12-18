from flask import Flask
from myapp.blueprints import main
from myapp.blueprints import api1
from myapp.blueprints import api2
from myapp.ext import database
from myapp.ext import styles


def create_app():
    app =  Flask(__name__)
    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'testeacert'
    
    database.init_app(app)
    styles.init_app(app)

    main.init_app(app)
    api1.init_app(app)
    api2.init_app(app)

    return app

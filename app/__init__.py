from flask import Flask



def create_app():
    app = Flask(__name__)

    from app.controller.user_controller import index
    app.add_url_rule('/', 'index', index)

    return app

# app/__init__.py
from flask import Flask
from .models import db

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///DB/entorno.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    with app.app_context():
        db.create_all()
        
        
    from .controller.user_controller import bp as user_bp
    app.register_blueprint(user_bp)
    return app


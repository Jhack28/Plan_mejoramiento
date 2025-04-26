from flask import Flask
from .models import db
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    from .controller.user_controller import bp as user_bp
    app.register_blueprint(user_bp)
    from app.controller.user_controller import index
    app.add_url_rule('/', 'index', index)
    return app

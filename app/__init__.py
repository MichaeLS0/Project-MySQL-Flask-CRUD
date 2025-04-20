from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
import os
import pymysql
pymysql.install_as_MySQLdb()

db = SQLAlchemy()

def create_app(config_class=Config):
    app = Flask(__name__, 
                template_folder=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'views', 'templates'))
    app.config.from_object(config_class)

    db.init_app(app)

    from app.controllers import main
    app.register_blueprint(main.bp)

    with app.app_context():
        db.create_all()

    return app 
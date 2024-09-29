import os
#import click

from flask import Flask, current_app
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate

from src.models import db

jwt = JWTManager()
migrate = Migrate()


#@click.command('init-db')
#def init_db_command():
#    """Clear the existing data and create new tables."""
#    global db
#    with current_app.app_context():
#        db.create_all()
#    click.echo('Initialized the database.')


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        SQLALCHEMY_DATABASE_URI='sqlite:///dio_bank.sqlite',
        JWT_SECRET_KEY='super-secret'
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    # app.cli.add_command(init_db_command)
    db.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)

    # registrando as rotas da aplicação
    from src.controllers import auth, role, post, user
    app.register_blueprint(user.app)
    app.register_blueprint(auth.app)
    app.register_blueprint(role.app)
    app.register_blueprint(post.app)

    return app
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate

# instantiate the db
db = SQLAlchemy()

def create_app(script_info=None):
    app = Flask(__name__)

    # Set configuration
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)
    app.config['JWT_SECRET_KEY'] = 'jwt-secret-string'
    
    jwt = JWTManager(app)

    # set up extensions
    db.init_app(app)
    migrate = Migrate(app, db)
    # register blueprints
    from project.api.users import users_blueprint
    app.register_blueprint(users_blueprint)

    @app.shell_context_processor
    def ctx():
        return { 'app': app, 'db': db }

    return app    
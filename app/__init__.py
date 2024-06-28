from flask import Flask
from app.extensions import migrate, db
from app.tour.models import Tour
from app.user.models import User
from app.config import Config
from app.user.views import user_bp
from app.tour.views import tour_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    register_extensions(app)
    register_blueprints(app)
    return app


def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db, render_as_batch=True)


def register_blueprints(app):
    bps = [user_bp, tour_bp]
    for bp in bps:
        app.register_blueprint(bp)

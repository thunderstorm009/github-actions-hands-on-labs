from flask import Flask
from .routes import api


def create_app(test_config=None):
    app = Flask(__name__)
    app.config["DATABASE"] = ":memory:" if test_config and test_config.get("TESTING") else "app.db"
    if test_config:
        app.config.update(test_config)
    from .db import init_app
    init_app(app)
    app.register_blueprint(api)
    return app

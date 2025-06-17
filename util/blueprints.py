from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint
from Blueprints.auth import auth_bp

def register_blueprints(app: Flask, testing=False):
    # Swagger documentation setup
    swaggerui_blueprint = get_swaggerui_blueprint(
        app.config["SWAGGER_URL"],
        app.config["API_URL"],
        config={"app_name": "Micro Service"},
    )

    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(swaggerui_blueprint, url_prefix=app.config["SWAGGER_URL"])

    return app

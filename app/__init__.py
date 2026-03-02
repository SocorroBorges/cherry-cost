from flask import Flask
from app.database import engine
from app.models import Base

def create_app():
    app = Flask(__name__)

    # Garante que tabelas existam
    Base.metadata.create_all(engine)

    from app.routes import main
    app.register_blueprint(main)

    return app
import os
from flask import Flask, jsonify, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from config import Config

# Initialize extensions (GLOBAL)
db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Enable CORS (clean + no warnings)
    CORS(
        app,
        resources={r"/api/*": {"origins": "*"}},
        supports_credentials=True
    )

    # 🔹 Import ALL models here (REQUIRED for flask db migrate)
    with app.app_context():
        from app.models.login import login
        from app.models.inventory import Inventory
        from app.models.quotation import Quotation

    # 🔹 Register Blueprints
    from app.routes.login_routes import login_bp
    from app.routes.inventory_routes import inventory_bp
    from app.routes.quotation_routes import quotations_bp

    app.register_blueprint(login_bp, url_prefix="/api")
    app.register_blueprint(inventory_bp)
    app.register_blueprint(quotations_bp, url_prefix="/api")

    # Serve uploaded files
    @app.route("/uploads/<path:filename>")
    def serve_uploaded_file(filename):
        upload_folder = os.path.join(os.getcwd(), "uploads")
        return send_from_directory(upload_folder, filename)

    # Health check
    @app.route("/")
    def health_check():
        return jsonify({"status": "healthy"})

    return app

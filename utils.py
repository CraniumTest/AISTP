from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def configure_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///aistp.db'
    db.init_app(app)
    with app.app_context():
        db.create_all()

# Additional functions for profile management, story interaction, etc.

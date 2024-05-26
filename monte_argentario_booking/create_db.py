from app import app, db
# from flask_migrate import Migrate

# migrate = Migrate(app, db)

with app.app_context():
    db.create_all()
    print("Database tables created!")

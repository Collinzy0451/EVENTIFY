from app import app, db
from sqlalchemy import text

# Push the application context
with app.app_context():
    # Test the database connection
    try:
        # This will try to connect and get the version of the database
        with db.engine.connect() as connection:
            connection.execute(text('SELECT 1'))
        print("Database connection successful!")

        # Create all tables
        db.create_all()
        print("Tables created successfully!")
    except Exception as e:
        print("Database connection failed:", str(e))
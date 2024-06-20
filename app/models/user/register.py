from app import db

class Registration(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    contact_no = db.Column(db.String(50), nullable=False)
    country_of_residence = db.Column(db.String(50), nullable=False)
    type_of_ticket = db.Column(db.String(50), nullable=False)
    num_of_ticket = db.Column(db.Integer, nullable=False)
    event_name = db.Column(db.String(100), nullable=False)
    event_venue = db.Column(db.String(100), nullable=False)
    eligibility = db.Column(db.String(100), nullable=False)
    event_date = db.Column(db.Date, nullable=False)


     


from app import db
import random, string

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
    unique_code = db.Column(db.String(4), unique=True, nullable=False)


    def __init__(self, *args, **kwargs):
        super(Registration, self).__init__(*args, **kwargs)
        self.generate_unique_code()

    def generate_unique_code(self):
        #generate a 4 digit code
        code = ''.join(random.choices(string.digits, k=4))

        #check if the code is unique
        while Registration.query.filter_by(unique_code=code).first() is not None:
            code = ''.join(random.choices(string.digits, k=4))

        self.unique_code = code


     


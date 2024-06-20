from app import app, db
from flask import render_template, request, redirect, url_for, flash
from app.models.user import Registration

@app.route('/register', methods=['GET', 'POST'])
def register_page():
    if request.method == 'POST':
        # Get the form data
        form_data = request.form

        # Create a registration object and add it to the database
        registration = Registration(
            first_name=form_data.get('first_name'),
            last_name=form_data.get('last_name'),
            email=form_data.get('email'),
            type_of_ticket=form_data.get('ticket_type'),
            num_of_ticket=form_data.get('number_of_tickets'),
            contact_no=form_data.get('contact_no'),
            country_of_residence=form_data.get('country_of_residence'),
            event_name=form_data.get('event_name'),
            event_venue=form_data.get('event_venue'),
            eligibility=form_data.get('eligibility'),
            event_date=form_data.get('event_date')
        )
        db.session.add(registration)
        db.session.commit()

        flash('You have successfully registered for the event!', 'congrats')

        # Redirect to the page of displaying the user inputs
        return redirect(url_for('user_inputs'))

    return render_template("root/register.html")

@app.route('/user_inputs')
def user_inputs():
    # Display all user inputs from the db
    registrations = Registration.query.all()

    return render_template('root/user_inputs.html', registrations=registrations)

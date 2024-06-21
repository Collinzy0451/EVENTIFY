from app import app, db, login_manager
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, login_required, logout_user
from app.models.admin import Admin

@login_manager.user_loader
def load_user(user_id):
    return Admin.query.get(int(user_id))


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    if request.method == 'POST':
        email = request.form.get('password')
        password = request.form.get('password')

        #check for any existing admin records

        existing_admin = Admin.query.first()

        if existing_admin:
            admin = Admin.query.filter_by(email=email, password=password).first()

            if admin:
                login_user(admin)
                return redirect(url_for('dashboard'))
            
            flash('Invalid email or password. Please try again', 'error')
            return render_template('admin/login.html')
        
        else:
            #If there is no admin record, create new admin.
            new_Admin = Admin(email=email, password=password)
            db.session.add(new_Admin)
            db.session.commit()

            #login admin

            login_user(new_Admin)
            return redirect(url_for('dashboard'))
        

    return render_template('admin/login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('you have been logged out')
    return redirect(url_for('login_page'))
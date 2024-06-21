from flask import render_template
from app import app
from flask_login import login_required

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('/admin/dashboard.html')
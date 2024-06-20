from flask import render_template
from app import app

@app.route('/dashboard')
def dashboard():
    return render_template('/admin/dashboard.html')
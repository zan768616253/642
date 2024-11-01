from flask import Blueprint, render_template, redirect, url_for, request, flash, session
from werkzeug.security import check_password_hash
from ..models import Customer, Staff, Person

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/')
def dashboard():
    try:
        if session['user_name']:
            if session['user_type'] == 'CUSTOMER':
                return redirect(url_for('customer.dashboard'))  # Redirect to dashboard or another appropriate page
            else:
                return redirect(url_for('staff.dashboard'))  # Redirect to dashboard or another appropriate page
        else:
            return redirect(url_for('auth.login'))  # Redirect to dashboard or another appropriate page
    except KeyError:
        return redirect(url_for('auth.login'))  # Redirect to login if session key doesn't exist

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        try:
            username = request.form['username']
            password = request.form['password']

            # Fetch user from the database
            user = Person.query.filter_by(username=username).first()

            if user and user.password == password:
                session['user_id'] = user.id
                session['user_type'] = user.type
                session['user_name'] = user.username
                flash('Login successful!', 'success')
                if user.type == 'CUSTOMER':
                    return redirect(url_for('customer.dashboard'))  # Redirect to dashboard or another appropriate page
                else:
                    return redirect(url_for('staff.dashboard'))  # Redirect to dashboard or another appropriate page
            else:
                flash('Invalid username or password', 'error')
        except Exception as e:
            flash(f'An error occurred during login: {str(e)}', 'error')
    return render_template('login.html')

@auth_bp.route('/logout')
def logout():
    try:
        session.clear()
        flash('Logged out successfully', 'success')
    except Exception as e:
        flash(f'An error occurred during logout: {str(e)}', 'error')
    return redirect(url_for('auth.login'))

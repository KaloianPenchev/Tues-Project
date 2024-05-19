from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/')
def home():
    return render_template('landing.html', user=current_user)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()

        if user is None:
            flash('Account does not exist.', category='error')

        if check_password_hash(user.password, password):
            login_user(user, remember=True)
        else:
            flash('Incorrect password, try again.', category='error')

    return render_template('login.html', user=current_user)
@auth.route('/logout', methods=['GET', 'POST'])
def logOut():
    return render_template('landing.html', user=current_user)

@auth.route('/register', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        confirmPassword = request.form.get('confirmPassword')
        user = User.query.filter_by(email=email).first()
        usern = User.query.filter_by(first_name=first_name).first()

        if user:
            flash('Email already exists.', category='error')
        elif usern:
            flash('Username already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif len(password) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            new_user = User(username=username, email=email, password=generate_password_hash(password, method='pbkdf2:sha256'), confirmPassword=confirmPassword)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
    return render_template('register.html', user=current_user)

@auth.route('/courses', methods=['GET', 'POST'])
def courses():
    return render_template('catalog.html')

@auth.route('/practice', methods=['GET', 'POST'])
def practice():
    return render_template('quest.html')

@auth.route('/tests', methods=['GET', 'POST'])
def tests():
    return render_template('upcomingtests.html')

@auth.route('/homeafterreg', methods=['GET', 'POST'])
def homeafterRegister():
    return render_template('home.html')

@auth.route('/discuss', methods=['GET', 'POST'])
def discuss():
    return render_template('discuss.html')
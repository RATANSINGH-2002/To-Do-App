from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user # SESSION IMPORTS
from Website import DB_Name
from .models import Attendee
from werkzeug.security import generate_password_hash, check_password_hash
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email_get = request.form.get('email')
        password_get = request.form.get('password','').strip()  # Prevent NoneType error

        if not email_get or not password_get:
            flash('Email and password are required.', category='error')
            return render_template("login.html", boolean=True)
        
        user = Attendee.query.filter_by(email=email_get).first()
        if user:
            if check_password_hash(user.password, password_get):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True) # THIS REMEMBERS THE USER UNLESS SERVER RESTART
                return redirect(url_for('views.home'))  # Redirect to home page
            else:
                flash('Incorrect password, try again...', category='error')
        else:
            flash('Email does not exist.', category='error')
    return render_template("login.html", user=current_user)

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        First_name = request.form.get('First_name','').strip() 
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        # print("Form Data:", request.form.to_dict()) # Checking if data is getting stored or not

        user = Attendee.query.filter_by(email=email).first()
        if user:
            flash('Email already exists...', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 4 characters.', category='error')
        elif len(First_name) < 2:
            flash('FirstName must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 3:
            flash('Password must be greater than 3 characters.', category='error')
        else:

            # Add user to database
            new_user = Attendee(email=email, First_name=First_name, password=generate_password_hash(password2, method='pbkdf2:sha256'))
            try:
                db.session.add(new_user)
                print(f"User ID before commit: {new_user.id}")  # Should be None before commit
                db.session.commit()
                print(f"User ID after commit: {new_user.id}")   # Should be assigned after commit
            except Exception as e:
                db.session.rollback()  # Rollback changes if any error occurs
                print(f"Database commit failed: {e}")  # Print error to console
            login_user(user, remember=True) # THIS REMEMBERS THE USER UNLESS SERVER RESTART
            flash('Account Created.', category='success')
            return redirect(url_for('views.home')) # IF SIGN UP SUCCESSFULLY REDIRECT TO HOME PAGE  
    return render_template("sign_up.html" , user = current_user)

@auth.route('/logout')
@login_required # Can't use this page unless login or sign is successful
def logout():
    logout_user() #clears the memory for login user
    return redirect(url_for('auth.login')) # iF LOGOUT THEN REDIRECT TO LOGIN PAGE

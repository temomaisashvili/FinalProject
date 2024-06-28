import os

from flask import Blueprint, request, flash, redirect, session, url_for, render_template
from bcrypt import hashpw, checkpw, gensalt

from app.user.models import User
from app.decorators import is_not_authenticated
from .forms import LoginForm, RegistrationForm
from app.extensions import db
template_folder = os.path.abspath('app/user/templates')
user_bp = Blueprint('user', __name__, template_folder=template_folder, url_prefix='/user')


@user_bp.route('/login', methods=['GET', 'POST'])
@is_not_authenticated
def login():
    form = LoginForm()
    if request.method == 'POST':

        if form.validate_on_submit():
            email = form.email.data
            password = form.password.data
            user = User.authenticate(email, password)
            if not user and not checkpw(password.encode('utf-8'), user.password):

                flash('Incorrect, Try Again!')
                return redirect('login')
            session['user_id'] = user.id
            return redirect(url_for('home'))
        return render_template('login.html', form=form)
    return render_template('login.html', form=form)


@user_bp.route('/register', methods=["POST", "GET"])
@is_not_authenticated
def register():
    form = RegistrationForm()
    if request.method == 'POST':
        print(form.data)
        if form.validate_on_submit():
            first_name = form.first_name.data
            last_name = form.last_name.data
            email = form.email.data
            password = form.password.data
            age = form.age.data
            address = form.address.data

            user = User.query.filter_by(first_name=first_name).first()

            if user is not None:
                flash('User With This First Name Already Exists!')
                return render_template('register.html', form=form, user=user)
            hashed_password = hashpw(password.encode('utf-8'), gensalt())
            user = User(first_name=first_name, last_name=last_name,
                        email=email, password=hashed_password,
                        age=age, address=address)
            db.session.add(user)
            db.session.commit()
            flash('User Successfully Created!!')
            return redirect(url_for('home'))
        print(form.errors)
        return render_template('register.html', form=form)
    return render_template('register.html', form=form)


@user_bp.route('/user_tours/<int:user_id>')
def user_tours(user_id):
    user = User.query.get(user_id)
    if not user:
        flash(f'User With ID={user_id} Does Not Exists!')
        return redirect(url_for('tours'))
    tours = user.tours
    return render_template('tours.html', tours=tours, user_id=user_id)

@user_bp.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('Successfully Logged Out')
    return redirect('login')

@user_bp.route('/')
@user_bp.route('/home')
def home():
    return render_template('index.html')

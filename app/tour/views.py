from flask import Blueprint, render_template, flash, redirect, url_for, request
import os

from app import Tour, User
from app.decorators import is_authenticated
from app.tour.forms import TourForm
from app.extensions import db


template_folder = os.path.abspath('app/templates')
tour_bp = Blueprint('tour', __name__, template_folder=template_folder, url_prefix='/tour')


@is_authenticated
@tour_bp.route('/tours', methods=['POST', 'GET'])
def tours():
    tour_data = Tour.query.all()
    user_data = User.query.all()
    return render_template('tour/tours.html', tour_data=tour_data, user_data=user_data)


@is_authenticated
@tour_bp.route('/create_tours/<int:user_id>', methods=['POST', 'GET'])
def create_tours(user_id):
    form = TourForm()
    user = db.session.get(User, user_id)
    if not user:
        flash(f'User With ID={user_id} Does Not Exists!')
        return redirect(url_for('tour.tours'))

    if request.method == 'POST':
        if form.validate_on_submit():
            title = form.title.data
            content = form.content.data
            tour = Tour(title=title, content=content)
            user.tours.append(tour)
            db.session.add(tour)
            db.session.commit()
            flash('Tour Successfuly Added')
            return redirect(url_for('user.user_tours', user_id=user_id))
        return render_template('tour/create_tours.html', form=form)

    return render_template('tour/create_tours.html', form=form, user_id=user_id)


from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models.user import User
from app import db

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    users = User.query.all()
    return render_template('index.html', users=users)

@bp.route('/user/<int:user_id>')
def user_detail(user_id):
    user = User.query.get_or_404(user_id)
    return render_template('user_detail.html', user=user)

@bp.route('/user/add', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        
        if User.query.filter_by(username=username).first():
            flash('Username already exists')
            return redirect(url_for('main.add_user'))
            
        if User.query.filter_by(email=email).first():
            flash('Email already exists')
            return redirect(url_for('main.add_user'))
            
        user = User(username=username, email=email)
        db.session.add(user)
        db.session.commit()
        
        flash('User added successfully')
        return redirect(url_for('main.index'))
        
    return render_template('add_user.html')

@bp.route('/user/edit/<int:user_id>', methods=['GET', 'POST'])
def edit_user(user_id):
    user = User.query.get_or_404(user_id)
    if request.method == 'POST':
        user.username = request.form['username']
        user.email = request.form['email']
        db.session.commit()
        flash('User updated successfully')
        return redirect(url_for('main.index'))
    return render_template('edit_user.html', user=user)

@bp.route('/user/delete/<int:user_id>', methods=['POST'])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    flash('User deleted successfully')
    return redirect(url_for('main.index'))

from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import  login_required, current_user
from website import db
from website.Models.models import Note

#this file is a blueprint of our application.Blueprint its just a way of separating our app, per tmos i definuar te gjitha views ne nje file

views = Blueprint('views',__name__)

@views.route('/', methods=['GET'])
def home():
    return render_template("home.html",user=current_user)




@views.route('/notes', methods=['GET','POST'])
@login_required
def notes():
    if request.method == 'POST':
        note = request.form.get('note')
        title = request.form.get('title')

        if len(note) < 1:
            flash('Note is too short', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id,title=title)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')
    return render_template("notes.html", user=current_user)

@views.route('/<int:id>/edit', methods=('GET', 'POST'))
@login_required
def edit(id):
    note = Note.query.filter_by(id=id).first()
    if request.method == 'POST':
        data = request.form['data']
        title = request.form['title']
        if not data:
            flash('Data is required!')
        else:
            note.data = data
            note.title = title
            db.session.commit()
            return redirect(url_for('views.notes'))

    return render_template('edit.html', note=note, user=current_user)


@views.route('/<int:id>/delete', methods=('POST',))
def delete(id):
    note = Note.query.filter_by(id=id).first()
    db.session.delete(note)
    db.session.commit()
    flash('Note with id "{}" was successfully deleted!'.format(id))
    return redirect(url_for('views.notes'))
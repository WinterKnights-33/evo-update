

from crypt import methods
from flask import render_template, redirect, request, session

from flask_app import app

from flask_app.models.apex import Apex

from flask_app.controllers.users import User

@app.route("/home")
def home():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        'id': session['user_id']
    }
    return render_template('homePage.html', user = User.get_with_id(data), apexes = Apex.get_all_types())

@app.route('/apex/view/<int:id>')
def view(id):
    data = {
        'id': id
    }
    return render_template('speculation.html', apex = Apex.get_one_type(data))

@app.route('/apex/edit/<int:id>')
def edit(id):
    data = {
        'id': id
    }
    return render_template('edit.html', apex = Apex.get_one_type(data))

@app.route('/addNew/apex/update/<int:id>', methods = ['POST'])
def update(id):
    data = {
        'id': id,
        'experiment_no': request.form['experiment_no'],
        'description': request.form['description'],
        'user_id': session['user_id'],
    }
    Apex.update(data)
    return redirect('/home')

@app.route('/apex/delete/<int:id>')
def destroy(id):
    data = {
        'id': id
    }
    Apex.destroy(data)
    return redirect('/home')

@app.route('apex/addNew/save', methods=['POST'])
def save():
#    if 'user_id' not in session:
#       return redirct('/logout')
    data = {
        'id': id,
        'experiment_no': request.form['experiment_no'],
        'description': request.form['description'],
        'user_id': session['user_id']
    }
    Apex.save(data)
    return redirect('/home')
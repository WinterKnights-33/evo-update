

from flask import render_template, redirect, session, request, flash

from flask_app import app

from flask_app.models.user import User

from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route('/')
def log():
    return render_template('login.html')

@app.route('/register', methods=['POST'])
def register():
#    if not User.validate_reg(request.form):
#        return redirect('/')
    data = {
        "first_name": request.form["first_name"],
#       "last_name": request.form["last_name"],
        "email": request.form["email"],
        "password": bcrypt.generate_password_hash(request.form["password"])
    }
    id = User.save(data)
    session["user_id"] = id
    session["name"] = request.form["first_name"]
    return redirect("/home")

@app.route('/login',methods=['POST'])
def login():
    user = User.get_w_email(request.form)
#fix this later: /home for the if not statements, it'll force it to login and go to the home screen but this is not how you want it so, change it when you have time
    if not user:
        flash("Invalid Informaion")
        return redirect('/home')
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash("Invalid Information")
        return redirect('/home')
    session['user_id'] = user.id
    session['name'] = user.first_name
    return redirect('/home')

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")
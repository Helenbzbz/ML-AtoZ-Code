from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

##CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
#Line below only required once, when creating DB. 


@app.route('/')
def home():
    return render_template("index.html", logged_in=current_user.is_authenticated)


@app.route('/register', methods = ['POST','GET'])
def register():
    if request.method == "POST":
        if User.query.filter_by(email=request.form.get('email')).first():
            flash("You've already signed up with that email, log in instead!")
            return redirect(url_for('register'))
        
        new_user = User(
            email = request.form['email'],
            password = generate_password_hash(request.form['password'], 'pbkdf2:sha256', 8),
            name = request.form['name']
        )
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        return redirect(url_for('secrets', name = new_user.name, logged_in=current_user.is_authenticated))
    return render_template("register.html")


@app.route('/login', methods = ['POST', "GET"])
def login():
    if request.method == "POST":
        email = request.form['email']
        password_entered = request.form['password']
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password_entered):
                login_user(user)
                return redirect(url_for('secrets', name = user.name, logged_in=current_user.is_authenticated))
            else:
                return render_template("login.html", message = "Password Incorrect, please try again", logged_in=current_user.is_authenticated)
        else:
            return render_template("login.html", message = "The email does not exist, please try again", logged_in=current_user.is_authenticated)
    return render_template("login.html")


@app.route('/secrets/<name>', methods = ['POST', "GET"])
@login_required
def secrets(name):
    return render_template("secrets.html", name = name, logged_in=current_user.is_authenticated)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/download')
@login_required
def download():
    return send_from_directory('/Users/jielanzheng/Desktop/Summer Plan/Summer 2023 Codes/100Day Python Bootcamp/Day 67 Authentication/static/files', "cheat_sheet.pdf")


if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from flask_wtf.form import _Auto
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

app = Flask(__name__)
app.config['SECRET_KEY'] = "PythonTest"

class MyForm(FlaskForm):
    email = StringField('email',validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired(), Length(min = 8)])
    submit = SubmitField(label = "Log In")

@app.route("/login", methods = ["GET", "POST"])
def login():
    login_form = MyForm()
    if login_form.validate_on_submit(): 
        if login_form.email.data == "admin@email.com" and login_form.password.data == "12345678":
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html', form = login_form)

@app.route("/")
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
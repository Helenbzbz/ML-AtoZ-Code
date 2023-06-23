from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv
from csv import writer


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location_url = StringField('Cafe Location on Google Maps (URL)', validators=[DataRequired(), URL()])
    open_time = StringField('Open Time e.g. 8AM', validators=[DataRequired()])
    close_time = StringField('Close Time e.g. 5:30PM', validators=[DataRequired()])
    coffee_rating = SelectField('Coffee Rating', choices = ["☕️☕️☕️☕️☕️", "☕️☕️☕️☕️", "☕️☕️☕️", "☕️☕️", "☕️", "✘"], validators=[DataRequired()])
    wifi_rating = SelectField('Wifi Strength Rating', choices = ["💪💪💪💪💪", "💪💪💪💪", "💪💪💪", "💪💪", "💪", "✘"], validators=[DataRequired()])
    power_rating = SelectField('Power Socket Availability', choices = ["🔌🔌🔌🔌🔌", "🔌🔌🔌🔌", "🔌🔌🔌", "🔌🔌", "🔌", "✘"], validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods = ["POST", "GET"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        cafe = form.cafe.data
        location_url = form.location_url.data
        open_time = form.open_time.data
        close_time = form.close_time.data
        coffee_rating = form.coffee_rating.data
        wifi_rating = form.wifi_rating.data
        power_rating = form.power_rating.data
        new_entry = [cafe, location_url, open_time, close_time, coffee_rating, wifi_rating, power_rating]
        with open("100Day Python Bootcamp/Day 62 Advanced Flask/cafe-data.csv", "a") as csv_file:
            writer_object = writer(csv_file)
            writer_object.writerow(new_entry)
            csv_file.close()
        return redirect(url_for('cafes'))
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('100Day Python Bootcamp/Day 62 Advanced Flask/cafe-data.csv', newline='') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
        print(list_of_rows)
    return render_template('cafes.html', cafes=list_of_rows, len=len)

if __name__ == '__main__':
    app.run(debug=True)

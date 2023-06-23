from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired
from wtforms.widgets import TextArea
import requests

movie_headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJiNDEwMmE1NmZkZmNiNDU5MTE0YTRjNTExOTVkMDdjYiIsInN1YiI6IjY0OTVlZTBlOWEzNThkMDBjNTY4OWM1ZSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.uUj3IvFbLgpEpcgoCiuXJh0ZBIjpYBZyuVCJwHF3vgk"
}

db = SQLAlchemy()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies-collection.db"
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
db.init_app(app)

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String, nullable = False)
    year = db.Column(db.Integer, nullable = False)
    description = db.Column(db.String, nullable = False)
    rating = db.Column(db.Float, nullable = True)
    ranking = db.Column(db.Integer, nullable = True)
    review = db.Column(db.String, nullable = True)
    img_url = db.Column(db.String, nullable = False)

# Create the database
with app.app_context():
    db.create_all()

# # Add entery into the database
# with app.app_context():
#     new_movie = Movie(
#     title="Phone Booth",
#     year=2002,
#     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#     rating=7.3,
#     ranking=10,
#     review="My favourite character was the caller.",
#     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
#     )
#     db.session.add(new_movie)
#     db.session.commit()

Bootstrap(app)

class UpdateForm(FlaskForm):
    rating = FloatField('Your Rating Out of 10. e.g. 7.5', validators=[DataRequired()])
    review = StringField('Your Review', validators=[DataRequired()], widget=TextArea())
    submit = SubmitField("Done")

class AddForm(FlaskForm):
    title = StringField('Movie Title', validators=[DataRequired()])
    submit = SubmitField("Add")

@app.route("/", methods = ["POST", "GET"])
def home():
    all_movies = Movie.query.order_by(Movie.rating.desc()).all()
    for i in range(len(all_movies)):
        all_movies[i].ranking = i+1
    db.session.commit()
    return render_template("index.html", movies = all_movies)

@app.route("/delete<id>")
def delete(id):
    with app.app_context():
        movie_review = db.session.execute(db.select(Movie).where(Movie.id == id)).scalar()
        db.session.delete(movie_review)
        db.session.commit()
    return redirect(url_for('home'))

@app.route("/edit<id>", methods = ["POST", "GET"])
def edit(id):
    form = UpdateForm()
    if form.validate_on_submit():
        review = form.review.data
        rating = form.rating.data
        with app.app_context():
            movie_review = db.session.execute(db.select(Movie).where(Movie.id == id)).scalar()
            movie_review.review = review
            movie_review.rating = rating
            db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", form = form)

@app.route("/add", methods = ["POST", "GET"])
def add():
    form = AddForm()
    if form.validate_on_submit():
        name = form.title.data
        response = requests.get(f"https://api.themoviedb.org/3/search/movie?query={name}&include_adult=true&language=en-US&page=1", headers=movie_headers)
        return render_template('select.html', movies = response.json()['results'])
    return render_template('add.html', form=form)

@app.route("/find<movie_id>")
def find(movie_id):

    url = f"https://api.themoviedb.org/3/movie/{movie_id}?language=en-US"
    response = requests.get(url, headers=movie_headers)

    movie_info = response.json() 
    title = movie_info['original_title']
    poster_path =  movie_info['poster_path']
    year = movie_info['release_date'].split("-")[0]
    description = movie_info['overview']

    if poster_path == None or year == None or year == None:
        print("This movie has missing information")
        return redirect(url_for('add', missing = "The movie you chose has missing info"))
    img_url = "https://image.tmdb.org/t/p/w500/"+movie_info['poster_path']

    with app.app_context():
        new_movie = Movie(
        title=title,
        year=year,
        description=description,
        img_url=img_url
        )
        db.session.add(new_movie)
        db.session.commit()

    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)

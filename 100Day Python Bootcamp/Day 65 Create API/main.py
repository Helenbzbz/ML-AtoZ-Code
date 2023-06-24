from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}

@app.route("/")
def home():
    return render_template("index.html")
    
## HTTP GET - Read Record
@app.route("/random")
def get_random_cafe():
    with app.app_context():
      cafes = Cafe.query.all()
      random_cafe = random.choice(cafes)
    return jsonify(cafe = random_cafe.to_dict())

@app.route("/all")
def get_all_cafes():
    with app.app_context():
      cafes = Cafe.query.all()
    return jsonify(cafe = [cafe.to_dict() for cafe in cafes])

@app.route("/search")
def search():
    with app.app_context():
        loc = request.args.get("loc")
        search_cafe = db.session.execute(db.select(Cafe).where(Cafe.location==loc)).first()
        if search_cafe:
            return jsonify(cafe = search_cafe[0].to_dict())
        else:
            return jsonify(error = {'Not Found': 'Sorry, we don\'t have a cafe at that location'})

def str_to_bool(arg_from_url):
    if arg_from_url in ['True', ' true', 'T', 't', 'Yes', 'yes', 'y', '1']:
        return True
    else:
        return False

@app.route("/add", methods = ['POST'])
def add():
    new_cafe = Cafe(
        name = request.form.get("name"),
        map_url = request.form.get("map_url"),
        img_url = request.form.get("img_url"),
        location = request.form.get("location"),
        seats = request.form.get("seats"),
        has_toilet = request.form.get("has_toilet"),
        has_wifi = request.form.get("has_wifi"),
        has_sockets = request.form.get("has_sockets"),
        can_take_calls = request.form.get("can_take_calls"),
        coffee_price = request.form.get("coffee_price")
        )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response = {'success':'Successfully added the new cafe'})

## HTTP POST - Create Record

## HTTP PUT/PATCH - Update Record

## HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)

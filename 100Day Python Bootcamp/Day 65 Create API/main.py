from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)

API = "helenzhengbzbz9120884"

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


## HTTP POST - Create Record
@app.route("/add", methods = ["GET", 'POST'])
def add():
    new_cafe = Cafe(
        name = request.form.get("name"),
        map_url = request.form.get("map_url"),
        img_url = request.form.get("img_url"),
        location = request.form.get("location"),
        seats = request.form.get("seats"),
        has_toilet = str_to_bool(request.form.get("has_toilet")),
        has_wifi = str_to_bool(request.form.get("has_wifi")),
        has_sockets = str_to_bool(request.form.get("has_sockets")),
        can_take_calls = str_to_bool(request.form.get("can_take_calls")),
        coffee_price = request.form.get("coffee_price")
        )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response = {'success':'Successfully added the new cafe'})


## HTTP PUT/PATCH - Update Record
@app.route("/update-price/<int:cafe_id>", methods = ["GET", "PATCH"])
def update(cafe_id):
    with app.app_context():
        new_price = request.args.get("new_price")
        cafe = db.session.query(Cafe).get(cafe_id)
    if cafe:
        cafe.coffee_price = new_price
        db.session.commit()
        return jsonify(response={"success": "Successfully updated the price."})
    else:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."})

## HTTP DELETE - Delete Record
@app.route("/report-closed/<int:cafe_id>", methods = ["GET", "DELETE"])
def delete(cafe_id):
    api_key = request.args.get("api")
    if api_key == API:
        with app.app_context():
            cafe = db.session.query(Cafe).get(cafe_id)
        if cafe:
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(response={"success": "Successfully updated the price."})
        else:
            return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."})
    else:
        return jsonify(error={"API Error": "Sorry the API Key is wrong."})

if __name__ == '__main__':
    app.run(debug=True)

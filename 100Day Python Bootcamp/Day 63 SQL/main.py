from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# Start Configuration
db = SQLAlchemy()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books-collection.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Define the Schemas
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True, nullable=False)
    author = db.Column(db.String, nullable = False)
    rating = db.Column(db.Float, nullable = False)

# # Create Table
# with app.app_context():
#     db.create_all()

# # Insert new entry
# new_book = Book(title="Harry Potter", author="J. K. Rowling", rating=9.3)
# with app.app_context():
#     db.session.add(new_book)
#     db.session.commit()

# # Read records
# with app.app_context():
#     all_books = Book.query.all()
#     book = db.session.execute(db.select(Book).where(Book.title == "Harry Potter")).scalar()

# # Update Records
# with app.app_context():
#     book_to_update = db.session.execute(db.select(Book).where(Book.title == "Harry Potter")).scalar()
#     book_to_update.title = "Harry Potter and the Chamber of Secrets"
#     db.session.commit() 

# # Delete Record
# book_id = 1
# with app.app_context():
#     book_to_delete = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
#     db.session.delete(book_to_delete)
#     db.session.commit()


@app.route('/')
def home():
    with app.app_context():
        all_books = Book.query.all()
    return render_template('index.html', books = all_books)


@app.route("/add", methods = ["GET", "POST"])
def add():
    if request.method == "POST":
        title = request.form.get("title")
        author = request.form.get("author")
        rating = request.form.get("rating")
        new_book = Book(title=title, author=author, rating=rating)
        with app.app_context():
            db.session.add(new_book)
            db.session.commit()
    return render_template('add.html')


if __name__ == "__main__":
    app.run(debug=True)


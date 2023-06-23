from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

all_books = []


@app.route('/')
def home():
    return render_template('index.html', books = all_books)


@app.route("/add", methods = ["GET", "POST"])
def add():
    if request.method == "POST":
        title = request.form.get("title")
        author = request.form.get("author")
        rating = request.form.get("rating")
        new_book = {'title': title, 'author': author, 'rating': int(rating)}
        all_books.append(new_book)
        print(all_books)
    return render_template('add.html')


if __name__ == "__main__":
    app.run(debug=True)


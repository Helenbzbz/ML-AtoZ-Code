from flask import Flask, render_template
from datetime import datetime
import requests

app = Flask(__name__)

# Get gender
def get_gender(name):
    response = requests.get(f"https://api.genderize.io?name={name}")
    return (response.json()['gender'])

# Get Age
def get_age(name):
    response = requests.get(f"https://api.agify.io?name={name}")
    return (response.json()['age'])

@app.route("/")
def copyright():
    year = datetime.now().year
    return render_template('index.html', year = year)

@app.route("/guess/<name>")
def guess(name):
    age = get_age(name)
    gender = get_gender(name)
    return render_template('guess.html', age = age, gender = gender, name = name)

@app.route("/blog")
def blog():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    posts = response.json()
    print(posts)
    return render_template("blog.html", posts=posts)

if __name__ == "__main__":
    app.run(debug=True)


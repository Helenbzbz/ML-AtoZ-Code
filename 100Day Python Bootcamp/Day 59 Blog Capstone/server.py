from flask import Flask, render_template
import requests

app = Flask(__name__)

api_endpoint = "https://api.npoint.io/3ac95f7ef79e15ddd0c6"

@app.route("/")
def home():
    response = requests.get(api_endpoint)
    posts = response.json()
    return render_template("index.html", posts = posts)

@app.route("/post/<blog_id>")
def post(blog_id):
    response = requests.get(api_endpoint)
    posts = response.json()
    for post in posts:
        if str(post['id']) == blog_id:
            curr_post = post
    return render_template("post.html", post = curr_post)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
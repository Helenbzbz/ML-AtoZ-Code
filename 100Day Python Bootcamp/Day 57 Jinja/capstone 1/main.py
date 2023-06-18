from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    posts = response.json()
    return render_template("index.html", posts=posts)

@app.route('/post/<blog_id>')
def blog(blog_id):
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    posts = response.json()
    for post in posts:
        if blog_id == str(post['id']):
            id_post = post
    return render_template("post.html", post=id_post)

if __name__ == "__main__":
    app.run(debug=True)

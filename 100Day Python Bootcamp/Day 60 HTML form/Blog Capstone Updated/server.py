from flask import Flask, render_template, request
import requests
from smtplib import SMTP

def send_email(body):
    destination_email = "helenbzbz@gmail.com"
    myemail = "pythontest8789@outlook.com"
    password = ""
    connection = SMTP("smtp.office365.com")
    connection.starttls()
    connection.login(user = myemail, password=password)
    connection.sendmail(from_addr=myemail, to_addrs=destination_email, 
                    msg = f"Subject:New Message\n\n{body}")
    connection.close()

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

@app.route("/contact", methods = ["POST", "GET"])
def contact():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']
        body = f"Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"
        send_email(body)
        return render_template("contact.html", message = "Successfully sent message")
    else:
        return render_template("contact.html", message = "Contact me")

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask
import random

app = Flask(__name__)
upper_limit = 1000
random_number = random.randint(0, upper_limit)

@app.route('/')
def initial_page():
    global random_number
    return f"<h1>Guess a number between 0 and {upper_limit}</h1>\
        <img src='https://media.giphy.com/media/Pj6w9VJQ9azYdVW9fd/giphy.gif'>"

@app.route('/<int:number>')
def page_reveals(number):
    if number < random_number:
        return "<b><h1 style='color:blue'>Too Low! Try again</h1></b>\
        <img src='https://media.giphy.com/media/3oz8xLd9DJq2l2VFtu/giphy.gif'>"
    if number == random_number:
        return "<b><h1 style='color:green'>You found me!</h1></b>\
        <img src='https://media.giphy.com/media/kfXJTsTzz0hx6zDfBn/giphy.gif'>"
    if number > random_number:
        return "<b><h1 style='color:red'>Too High! Try again</h1></b>\
        <img src='https://media.giphy.com/media/ceeN6U57leAhi/giphy.gif'>"


if __name__ == "__main__":
    app.run(debug=True)
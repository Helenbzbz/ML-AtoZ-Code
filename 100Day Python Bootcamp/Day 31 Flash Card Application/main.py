BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *

FONT_LANGUAGE = ("Ariel", 40, "italic")
FONT_WORD = ("Ariel", 60, "bold")

french_word = "trou"

# ---------------------------------- UI/UX Setup ----------------------------------
window = Tk()
window.title("Flashy")
window.config(padx=50, pady = 50, bg = BACKGROUND_COLOR)

# Setup Card Front
card_front = Canvas(width = 800, height = 526, bg = BACKGROUND_COLOR, highlightthickness=0)
front_img = PhotoImage(file = '100Day Python Bootcamp/Day 31 Flash Card Application/images/card_front.png')
card_front.create_image(400, 263, image = front_img)
card_front.grid(column = 1, row = 1, columnspan=2)

language_text_front = card_front.create_text(400, 150, text = "French", fill = "black", font = FONT_LANGUAGE)
word_text_front = card_front.create_text(400, 263, text = french_word, fill = "black", font = FONT_WORD)

# Setup yes and no
wrong = Canvas(width = 400, height = 150, bg = BACKGROUND_COLOR, highlightthickness=0)
right = Canvas(width = 400, height = 150, bg = BACKGROUND_COLOR, highlightthickness=0)
wrong_img = PhotoImage(file = '100Day Python Bootcamp/Day 31 Flash Card Application/images/wrong.png')
right_img = PhotoImage(file = '100Day Python Bootcamp/Day 31 Flash Card Application/images/right.png')

wrong.create_image(200, 75, image = wrong_img)
wrong.grid(column = 1, row = 2)
right.create_image(200, 75, image = right_img)
right.grid(column = 2, row = 2)

window.mainloop()
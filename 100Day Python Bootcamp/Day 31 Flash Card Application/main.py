from tkinter import *
import pandas as pd
import random
import time

BACKGROUND_COLOR = "#B1DDC6"
FONT_LANGUAGE = ("Ariel", 40, "italic")
FONT_WORD = ("Ariel", 60, "bold")
TIME_TO_FLIP = 3000

timer = None
word = None

# ---------------------------- FLIP MECHANISM ------------------------------- # 
def flip():
    card.itemconfig(card_image, image = back_img)
    card.itemconfig(language_text, text = "English", fill = "white")
    card.itemconfig(word_text, text = word['English'], fill = "white")

# ---------------------------- COUNT MECHANISM ------------------------------- # 
def shuffle():
    global timer
    french_word_selection()
    card.itemconfig(card_image, image = front_img)
    card.itemconfig(language_text, text = "French", fill = "black")
    card.itemconfig(word_text, text = word['French'], fill = "black")
    timer = window.after(TIME_TO_FLIP, flip)

# ---------------------------------- FRENCH WORD ----------------------------------
def french_word_selection():
    french_word_data = pd.read_csv("100Day Python Bootcamp/Day 31 Flash Card Application/data/words_to_learn.csv")
    french_word_dict = french_word_data.to_dict(orient="records")
    global word
    word = random.choice(french_word_dict)

# -------------------------------- KNOW WORD  ------------------------------------
def know():
    window.after_cancel(timer)
    french_word_data = pd.read_csv("100Day Python Bootcamp/Day 31 Flash Card Application/data/words_to_learn.csv")
    french_word_data.drop(french_word_data[french_word_data['French'] == word['French']].index, inplace  = True)
    french_word_data.to_csv("100Day Python Bootcamp/Day 31 Flash Card Application/data/words_to_learn.csv", index = False)
    shuffle()

# ---------------------------------- UI/UX Setup ----------------------------------
window = Tk()
window.title("Flashy")
window.config(padx=50, pady = 50, bg = BACKGROUND_COLOR)

# Setup Card Front
card = Canvas(width = 800, height = 526, bg = BACKGROUND_COLOR, highlightthickness=0)
front_img = PhotoImage(file = '100Day Python Bootcamp/Day 31 Flash Card Application/images/card_front.png')
back_img = PhotoImage(file = '100Day Python Bootcamp/Day 31 Flash Card Application/images/card_back.png')
card_image = card.create_image(400, 263, image = front_img)
card.grid(column = 1, row = 1, columnspan=2)

try: 
    french_word_data = pd.read_csv("100Day Python Bootcamp/Day 31 Flash Card Application/data/words_to_learn.csv")
except FileNotFoundError:
    french_word_data = pd.read_csv("100Day Python Bootcamp/Day 31 Flash Card Application/data/french_words.csv")
    french_word_data.to_csv("100Day Python Bootcamp/Day 31 Flash Card Application/data/words_to_learn.csv", index = False)

french_word_selection()
language_text = card.create_text(400, 150, text = "French", fill = "black", font = FONT_LANGUAGE)
word_text = card.create_text(400, 263, text = word['French'], fill = "black", font = FONT_WORD)

# Setup yes and no
wrong_img = PhotoImage(file = '100Day Python Bootcamp/Day 31 Flash Card Application/images/wrong.png')
wrong_button = Button(image = wrong_img, bg = BACKGROUND_COLOR, highlightthickness=0, command = shuffle)
right_img = PhotoImage(file = '100Day Python Bootcamp/Day 31 Flash Card Application/images/right.png')
right_button = Button(image = right_img, bg = BACKGROUND_COLOR, highlightthickness=0, command = know)

wrong_button.grid(column = 1, row = 2)
right_button.grid(column = 2, row = 2)

shuffle()

window.mainloop()
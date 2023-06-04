from tkinter import *
from math import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
check = "✔️"
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text = "00:00")
    title.config(text = "Timer")
    checkmark.config(text = "")

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    if reps %8 == 0:
        count_down(60*LONG_BREAK_MIN)
        title.config(text = "Long Break", fg = RED)
    elif reps %2 == 0:
        count_down(60*SHORT_BREAK_MIN)
        title.config(text = "Short Break", fg = PINK)
    else:
        count_down(60*WORK_MIN)
        title.config(text = "Work", fg = GREEN)
    checkmark.config(text = f"{check*int(reps/2)}")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
import time
def count_down(count):
    minute = floor(count/60)
    second = count%60
    
    if second < 10:
        second = f'0{second}'
    canvas.itemconfig(timer_text, text = f"{minute}:{second}")

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady = 50, bg = YELLOW)

# Setup the timer word
title = Label(text="Timer", fg = GREEN, bg = YELLOW, font = (FONT_NAME, 35))
title.grid(column = 2, row = 1)
checkmark = Label(fg = GREEN, bg = YELLOW, font = (FONT_NAME, 10))
checkmark.grid(column = 2, row = 4)

# Setup Tomatto
canvas = Canvas(width = 200, height = 224, bg = YELLOW, highlightthickness=0)
totmato_img = PhotoImage(file = '100Day Python Bootcamp/Day 28 Pomodoro/tomato.png')
canvas.create_image(100, 112, image = totmato_img)
canvas.grid(column = 2, row = 2)
timer_text = canvas.create_text(100, 130, text = "00:00", fill = "white", font = (FONT_NAME, 35, "bold"))



# Set up Button
start_button = Button(text="Start", highlightthickness=0,command=start_timer)
reset_button = Button(text = "Reset", highlightthickness=0, command=reset_timer)
start_button.grid(column = 1, row = 3)
reset_button.grid(column = 3, row = 3)

window.mainloop()

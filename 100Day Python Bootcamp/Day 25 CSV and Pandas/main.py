import turtle 
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "100Day Python Bootcamp/Day 25 CSV and Pandas/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states_data = pd.read_csv("100Day Python Bootcamp/Day 25 CSV and Pandas/50_states.csv")
all_states = states_data["state"].to_list()
guess_states = []

state_guess = 0

drawer = turtle.Turtle()
drawer.penup()
drawer.hideturtle()

def draw_location(state, x, y):
    drawer.goto(x, y)
    drawer.write(state, font=("Arial", 13, "normal"))

game_is_on = True

while game_is_on:
    answer_state = screen.textinput(title = f"Guess the State {state_guess}/50", prompt = "What's another state")
    if answer_state == "Exit":
        missing_state = []
        for state in all_states:
            if state not in guess_states:
                missing_state.append(state)
        new_data = pd.DataFrame(missing_state)
        new_data.to_csv("100Day Python Bootcamp/Day 25 CSV and Pandas/Missing_State.csv")
        game_is_on = False

    if answer_state in all_states:
        state_data = states_data[states_data["state"] == answer_state]
        draw_location(answer_state, int(state_data["x"]), int(state_data["y"]))
        guess_states.append(answer_state)
        state_guess += 1

screen.exitonclick()
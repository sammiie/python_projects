import pandas as pd
import turtle

screen = turtle.Screen()
screen.title("Nigeria States Game")
image = "NGA_map.gif"
screen.addshape(image)
turtle.shape(image)
pen = turtle.Turtle()
pen.penup()
pen.hideturtle()

state_data = pd.read_csv("36_states.csv")
score = 0
game_on = True

all_state = list(state_data.state)
solved_state = []
while game_on and score < 36:
    guess = screen.textinput(title=f"{score}/36 States Correct", prompt="What's another state's name? Enter Exit to "
                                                                        "leave the game").title()

    if guess == "Exit":
        unsolved_states = []

        for elem in all_state + solved_state:
            if elem not in all_state or elem not in solved_state:
                unsolved_states.append(elem)
        df = pd.DataFrame(unsolved_states, columns=["States to learn"])
        df.to_csv("states_to_learn.csv")
        break

    for states in state_data.state:
        if states == guess:
            solved_state.append(guess)
            score += 1
            x_cor = int(state_data[state_data.state == states].x)
            y_cor = int(state_data[state_data.state == states].y)
            pen.goto(x_cor, y_cor)
            pen.write(guess)



import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S_State_Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


data = pd.read_csv("50_states.csv")
state_list = data.state.to_list()
guess_state = []

while len(guess_state) < 50:
    answer = screen.textinput(title=f"{len(guess_state)}/50 States Correct ",
                              prompt="what's another state name? ").title()
    if answer == "Exit":
        state_to_learn = [state for state in state_list if state not in guess_state]
        print(state_to_learn)
        remaining_state = pd.DataFrame(state_to_learn)
        remaining_state.to_csv("state_to_learn.csv")
        break
    if answer in state_list:
        guess_state.append(answer)
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        selected_state = data[data.state == answer]
        x_state = int(selected_state.x)
        y_state = int(selected_state.y)
        t.goto(x_state, y_state)
        # t.write(selected_state.state.item()) = use to select the first element of a line with many information
        t.write(answer)








#print(data)


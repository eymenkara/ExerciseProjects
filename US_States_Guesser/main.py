import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)
data = pd.read_csv("50_states.csv")
correct_guesses = 0


# check if answer is correct
def correct(df, ans: str):
    if sum(df["state"] == ans) == 1:
        return True
    else:
        return False


turt = turtle.Turtle()
turt.hideturtle()
turt.penup()
learn = data["state"].to_list()



game_on = True
while game_on:

    if correct_guesses == 50:
        turt.goto(x=0, y=0)
        turt.write("You Won!", move=False, align="center", font=("Arial", 50, "bold"))
        game_on = False
    else:
        state_answer = screen.textinput(title=f"{correct_guesses}/50 States Correct",
                                        prompt="Guess a state name:").title()
        if state_answer == "Exit":
            break

        if state_answer == "Learn":
            print(learn)
            break

        if correct(data, state_answer):
            correct_guesses += 1
            learn.remove(state_answer)
            answer = data[data["state"] == state_answer]
            turt.goto(x=int(answer["x"]), y=int(answer["y"]))
            turt.write(state_answer, move=False, align="left", font=("Arial", 11, "normal"))

screen.exitonclick()

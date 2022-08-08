import pandas
import turtle

screen = turtle.Screen()
screen.title("U.S. States Games")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

state_data = pandas.read_csv("50_states.csv")
state_names = state_data.state.to_list()
missing_state = state_names

write_name = turtle.Turtle()
write_name.hideturtle()
write_name.penup()
FONT = 'Courier', 10, 'italic'
right_count = 0

while right_count < 50:
    answer_state = screen.textinput(title=f"{right_count}/50 States Correct",
                                    prompt="What's another state's name?").capitalize()
    if answer_state == 'Exit':
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("Missing States.csv")
        break
    if answer_state in state_names:
        state = state_data[state_data.state == answer_state]
        x_cor = state.x
        y_cor = state.y
        write_name.goto(int(x_cor), int(y_cor))
        write_name.write(answer_state, align='center', font=FONT)
        right_count += 1
        missing_state.remove(answer_state)



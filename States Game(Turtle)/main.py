import turtle
import pandas
from location import Goto
data=pandas.read_csv("50_states.csv")
list_of_states=data.state.to_list()
X_corrdinates=data.x.to_list()
Y_coordinates=data.y.to_list()
print(list_of_states)

screen=turtle.Screen()
timmy=turtle.Turtle()


screen.addshape("blank_states_img.gif")
timmy.shape("blank_states_img.gif")

is_on=True
while is_on:
    response = turtle.textinput("Input", "Name the State.").title()
    print(type(response))
    for index,state in enumerate(list_of_states):
        if response==state:
            xx=X_corrdinates[index]
            yy=Y_coordinates[index]
            goto=Goto(xx,yy)
            goto.to_write(response)
        elif response=="exit":
            is_on=False



screen.exitonclick()
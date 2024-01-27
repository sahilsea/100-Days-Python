import turtle
import pandas

# Create the Screen for the Game
screen = turtle.Screen()
screen.title("Bihar District Guessing Game")
image = "bihar90.gif"
screen.setup(width= 1000)
screen.addshape(image)
turtle.shape(image)


# Challange 
score = 0
guessed_state = []
data = pandas.read_csv("Bihar_states_coordinates.csv")
# Getting answer By providing a prompt.
# Storing all states in a list
all_states = data.state.to_list()


# Checking if the state that user entered , exist in the list of all states
while len(guessed_state) < 38:
    answer = screen.textinput(title= f"Guessed Districts = {score}/38", prompt= "Guess another State" ).title()
    if answer == "Exit":
        break
    if answer in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        # Getting the data of the state entered by the user
        state_i = data[data['state'] == answer]
        t.goto(x= int(state_i.x), y= int(state_i.y))
        t.write(arg= f'{answer}', move= False, align= 'center', font= ("Bold", 19, "normal"))
        guessed_state.append(answer)
        score += 1

# States that you missed
missed_state = []
for state in all_states:
    if state not in guessed_state:
        missed_state.append(state)

missed_state_Frame = pandas.DataFrame(missed_state)
missed_state_Frame.to_csv("States_to_learn.csv")



# def get_click_coor(x,y):
#     print(x,y)

# turtle.onscreenclick(get_click_coor)
# turtle.mainloop()



screen.exitonclick()
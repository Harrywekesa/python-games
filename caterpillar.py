#You use the four arrow keys to steer a caterpillar around the screen and make it “eat” leaves. Each leaf gives you a
#point, but it also makes the caterpillar bigger and faster, making the game harder. Keep the caterpillar inside the
#game window, or the game’s over!
#This project uses two main turtles: one to draw the caterpillar and one to draw the leaves.

import random
import turtle as t

t.bgcolor('yellow')
caterpillar = t.Turtle()
caterpillar.shape('square')
caterpillar.color('red')
caterpillar.speed(0) #Prevents the turtle moving before the game starts
caterpillar.penup()
caterpillar.hideturtle()

leaf = t.Turtle()
leaf_shape = ((0, 0), (14, 2), (18, 6), (20, 20),(6, 18), (2, 14))
t.register_shape('leaf', leaf_shape)
leaf.shape('leaf')
leaf.color('green')
leaf.penup()
leaf.hideturtle()
leaf.speed(0)

#two more turtles to add text to the game. One will display a message before the action starts,
#telling players to press the space bar to begin. The other will write the score in the corner of the window
game_started = False
text_turtle = t.Turtle()
text_turtle.write('Press SPACE to start', align = 'center', font = ('arial', 16, 'bold'))
text_turtle.hideturtle()

score_turtle = t.Turtle()
score_turtle.hideturtle()
score_turtle.speed(0)

def game_over():
    caterpillar.color('yellow')
    leaf.color('yellow')
    t.penup()
    t.hideturtle()
    t.write('GAME OVER', align = 'center', font = ('Arial',30 , 'normal'))
#The center of the window has the coordinates (0, 0). Since the window is 400 wide, the right
#wall is half the width from the center, which is 200. The code gets the left wall’s position by
#subtracting half the width from 0. In other words, 0–200, which is –200. It finds the position of the
#top and bottom walls by a similar method.

def outside_window():  # sourcery skip: inline-immediately-returned-variable
    left_wall = -t.window_width()/2 
    right_wall = t.window_width()/2 
    top_wall = t.window_height()/2
    bottom_wall = -t.window_height()/2
    (x, y) = caterpillar.pos()
    outside = x < left_wall or x > right_wall or y > top_wall or y < bottom_wall
    return outside
    

def display_score(current_score):
    score_turtle.clear()
    score_turtle.penup()
    x = (t.window_width()/2) - 50 #50 pixels from the right
    y = (t.window_height()/2) - 50 #50 pixels from the top
    score_turtle.setpos(x, y)
    score_turtle.write(str(current_score), align = 'right', font = ('Arial', 40, 'bold'))
    

def place_leaf():
    leaf.ht()  #ht is short for hideturtle.
    leaf.setx(random.randint(-200, 200))
    leaf.sety(random.randint(-200, 200))
    leaf.st() #st is short for showturtle.

def start_game():
    global game_started
    if game_started:
        return
    
    
    game_started = True
    score = 0
    text_turtle.clear()
    caterpillar_speed = 2
    caterpillar_length  = 3
    caterpillar.shapesize(1,caterpillar_length, 1)
    caterpillar.showturtle()
    display_score(score)
    place_leaf()
    
    
    while True:
        caterpillar.forward(caterpillar_speed)
        if caterpillar.distance(leaf) < 20: #The caterpillar eats the leaf when it’s less than 20 pixels away.
            place_leaf() #The current leaf has been eaten, so add a new leaf.
            #This will make the caterpillar grow longer.
            caterpillar_length =+ 10
            caterpillar.shapesize(1, caterpillar_length, 1)
            caterpillar_speed += 1
            score += 10
            display_score(score)
        if outside_window():
            game_over()
            break
def move_up():  # sourcery skip: merge-comparisons
    #Check if the caterpillar is heading left or right.
    if caterpillar.heading() == 0 or caterpillar.heading() == 180 :
        caterpillar.setheading(90)
        
def move_down():  # sourcery skip: merge-comparisons
    if caterpillar.heading() == 0 or caterpillar.heading() == 180 :
        caterpillar.setheading(270)
        
def move_left():  # sourcery skip: merge-comparisons 
    if caterpillar.heading() == 90 or caterpillar.heading() == 270 :
        caterpillar.setheading(180)      
        
def move_right():  # sourcery skip: merge-comparisons
    if caterpillar.heading() == 90 or caterpillar() == 270 :
        caterpillar.setheading(0)
        
t.onkey(start_game, 'space')
t.onkey(move_up, 'Up')
t.onkey(move_down, 'Down')
t.onkey(move_right, 'Right')
t.onkey(move_left, 'Left')

t.listen()
t.mainloop()
    

                  
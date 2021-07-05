#requires a sharp eye and lightning-fast reactions. It works just like the card game but uses colored shapes that appear on the
#screen rather than cards that are dealt
#Different shapes appear on the screen at random in either black, red, green, or blue. If a color appears twice in succession, hit the
#snap key. Player 1 presses the “q” key to snap and player 2 the “p” key. Each correct snap scores a point. Snap at the wrong time and
#you lose a point. The player with the highest score is the winner.

import random
import time
from tkinter import Tk, Canvas, NORMAL, HIDDEN
from turtle import Shape   #HIDDEN lets you hide each shape until you want to show it with 
#NORMAL—otherwise all the shapes will appear on the screen at the start of the game

root = Tk()
root.title('Snap')

#Creating the canvas
c = Canvas(root,width=400, height=400)

shapes = []
#This creates four circles of the same size—one each in black, red, green, and blue—and adds them to the shapes list.
circle = c.create_oval(35, 20, 365, 350, outline = 'black', fill='black', state = HIDDEN)
shapes.append(circle)
circle = c.create_oval(35, 20, 365, 350,outline = 'red', fill='red', state = HIDDEN)
shapes.append(circle)
circle = c.create_oval(35, 20, 365, 350, outline = 'green', fill='green', state = HIDDEN)
shapes.append(circle)
circle = c.create_oval(35,20, 365, 350, outline='blue', fill='blue', state = HIDDEN)
shapes.append(circle)
circle = c.create_oval(35,20, 365, 350, outline='orange', fill='orange', state = HIDDEN)
shapes.append(circle)
circle = c.create_oval(35,20, 365, 350, outline='indigo', fill='indigo', state = HIDDEN)
shapes.append(circle)
circle = c.create_oval(35,20, 365, 350, outline='violet', fill='violet', state = HIDDEN)
shapes.append(circle)
c.pack() #This line puts the shapes onto the canvas.

rectangle = c.create_rectangle(35, 100, 365, 270, outline = 'black', fill='black', state = HIDDEN)
shapes.append(rectangle)
rectangle = c.create_rectangle(35, 100, 365, 270, outline = 'red', fill='red', state = HIDDEN)
shapes.append(rectangle)
rectangle = c.create_rectangle(35, 100, 365, 270, outline = 'green', fill='green', state = HIDDEN)
shapes.append(rectangle)
rectangle = c.create_rectangle(35, 100, 365, 270, outline = 'blue', fill='blue', state = HIDDEN)
shapes.append(rectangle)
rectangle = c.create_rectangle(35, 100, 365, 270, outline = 'orange', fill='orange', state = HIDDEN)
shapes.append(rectangle)
rectangle = c.create_rectangle(35, 100, 365, 270, outline = 'indigo', fill='indigo', state = HIDDEN)
shapes.append(rectangle)
rectangle = c.create_rectangle(35, 100, 365, 270, outline = 'violet', fill='violet', state = HIDDEN)
shapes.append(rectangle)
c.pack()

square = c.create_rectangle(35, 20, 365, 350, outline = 'black', fill = 'black', state = HIDDEN)
shapes.append(square)
square = c.create_rectangle(35, 20, 365, 350, outline = 'red', fill = 'red', state = HIDDEN)
shapes.append(square)
square = c.create_rectangle(35, 20, 365, 350, outline = 'green', fill = 'green', state = HIDDEN)
shapes.append(square)
square = c.create_rectangle(35, 20, 365, 350, outline = 'blue', fill = 'blue', state = HIDDEN)
shapes.append(square)
square = c.create_rectangle(35, 20, 365, 350, outline = 'orange', fill = 'orange', state = HIDDEN)
shapes.append(square)
square = c.create_rectangle(35, 20, 365, 350, outline = 'indigo', fill = 'indigo', state = HIDDEN)
shapes.append(square)
square = c.create_rectangle(35, 20, 365, 350, outline = 'violet', fill = 'violet', state = HIDDEN)
shapes.append(square)
c.pack()

#To ensure that the shapes don’t appear in the same order each time, you need to shuffle them
random.shuffle(shapes)

shape = None
previous_color = " "
current_color = " "
player1_score = 0
player2_score = 0

def next_shape():
    #Using the global keyword ensures that changes to the variables are seen throughout the program.
    global shape
    global previous_color
    global current_color
    
    previous_color = current_color #This line sets previous_color to current_color before the code gets the next shape.

    c.delete(shape)
    
    if len(shapes) > 0:
        shape = shapes.pop(0) #Get the next shape if there are any shapes left.
        c.itemconfigure(shape, state = NORMAL) #Make the new shape visible
        current_color = c.itemcget(shape, 'fill') #Assign current color to the color of the new shape
        root.after(1000, next_shape)
    else:
        c.unbind('q')#hese lines stop the program responding to snaps after the game is over.
        c.unbind('p')
        if player1_score > player2_score:
            c.create_text(200, 200, text='WINNER : Player 1')
        elif player2_score > player1_score:
            c.create_text(200, 200, text = 'WINNER : Player 2')
        else:
            c.create_text(200, 200, text = 'DRAW')
        c.pack()
        
def snap(event):
    global shape
    global player1_score
    global player2_score
    valid = False
    
    c.delete(shape)
    
    if previous_color == current_color:
        valid = True
        
    if valid:
        if event.char == 'q':
            player1_score += 1
        else:
            player2_score += 1
        shape = c.create_text(200, 200, text = 'SNAP! You score 1 point') #Shown when the player snaps the wrong time
    else:
        if event.char == 'p':
            player1_score -= 1
        else:
            player2_score -= 1
        shape = c.create_text(200, 200, text = 'SNAP! Wrong answer! You lose a point')
#create a 3-second delay before the first shape appears. This gives the player time to
#find the Tkinter window in case it’s hidden behind other windows on the desktop
root.after(3000, next_shape) #The program waits for 3,000 milliseconds, or 3 seconds before showing the next shape.

c.bind('q', snap) #Key, function
c.bind('p', snap)
c.focus_set()
root.mainloop()

c.pack()
root.update_idletasks() #This line forces the program to update the GUI with the snap message immediately.
time.sleep(1) #Wait  1second for the players to read the message
        
        


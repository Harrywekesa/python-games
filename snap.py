#requires a sharp eye and lightning-fast reactions. It works just like the card game but uses colored shapes that appear on the
#screen rather than cards that are dealt
#Different shapes appear on the screen at random in either black, red, green, or blue. If a color appears twice in succession, hit the
#snap key. Player 1 presses the “q” key to snap and player 2 the “p” key. Each correct snap scores a point. Snap at the wrong time and
#you lose a point. The player with the highest score is the winner.

import random
import time
from tkinter import Tk, Canvas, NORMAL, HIDDEN   #HIDDEN lets you hide each shape until you want to show it with 
#NORMAL—otherwise all the shapes will appear on the screen at the start of the game

root = Tk()
root.title('Snap')

#Creating the canvas
c = Canvas(root,width=400, height=400)

shapes = []
#This creates four circles of the same size—one each in black, red, green, and blue—and adds them to the shapes list.
circle = c.create_oval(35, 20, 365, 350, outline = 'balck', fill='black', state = HIDDEN)
shapes.append(circle)
circle = c.create_oval(35, 20, 365, 350,outline = 'red', fill='red', state = HIDDEN)
shapes.append(circle)
circle = c.create_oval(35, 20, 365, 350, outline = 'green', fill='green', state = HIDDEN)
shapes.append(circle)
circle = c.create_oval(35,20, 365, 350, outline='blue', fill='blue', state = HIDDEN)
shapes.append(circle)
c.pack() #This line puts the shapes onto the canvas.




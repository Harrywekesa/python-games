#How good is your memory? Test it in this fun game where you have to find pairs of
#matching symbols. See how quickly you can find all 12 matching pairs!
import random
import tkinter
from tkinter import Tk, Button, DISABLED #DISABLED stops a button from responding after its symbol has been matched.
import time

root =  Tk()
root.title('Matchmaker')
root.resizable(width = False, height = False)


buttons = {}
first = True
previousX = 0
previousY = 0

button_symbols = {}
symbols = [u'\u2702', u'\u2702', u'\u2705', u'\u2705', u'\u2708', u'\u2708',
u'\u2709', u'\u2709', u'\u270A', u'\u270A', u'\u270B', u'\u270B',
u'\u270C', u'\u270C', u'\u270F', u'\u270F', u'\u2712', u'\u2712',
u'\u2714', u'\u2714', u'\u2716', u'\u2716', u'\u2728', u'\u2728'] #Unicode values for shapes

random.shuffle(symbols) #The shuffle() function from the random module mixes up the shapes.

#The outer x loop will work from left to right across the six columns, while the inner y loop will work from top
#to bottom down each column.Once the loops have run, each button will have been given a pair of x and y
#coordinates that set its position on the grid.

#The command parameter tells the program what to do when a button is pressed. This is a function
#call. In our program, it calls a lambda function. The width and height parameters are used to set
#the size of the button.

#Each time the loop runs, the lambda function saves the current button’s x and y values (the row and column it’s in).
#When the button’s pressed, it calls the show_symbol()function with these values,
#so the function which button has been pressed and which symbol to reveal.

#Each time the outer loop runs, the inner loop runs four times. So in total, the inner loop runs 6 x 4 = 24 times.

for x in range(6):
    for y in range(4):
        button = Button(command = lambda x = x, y = y : show_symbol(x, y), width = 3, height = 3)
        button.grid(column = x, row = y)
        buttons[x, y] = buttons
        button_symbols[x, y] = symbols.pop()

#This function will always display a symbol, but how it operates depends on whether
#it’s the first or second turn in the matching attempt. If it’s the first turn, the
#function just needs to remember which button was pressed. If it’s the second
#turn, it needs to check if the symbols match. Symbols that don’t match are
#hidden. Matching symbols are left showing and their buttons are disabled.
def show_symbol(x, y): #The x and y values tell the function which button has been pressed.
    global first
    global previousX,previousY
    buttons[x, y]['text'] = button_symbols[x, y]
    buttons[x, y].update()
    
    if first:
        previousX = x
        previousY = y
        first = False
    elif previousX != x or previousY != y:
        if buttons[previousX, previousY]['text'] != buttons[x, y]['text']: #If the symbols don’t match...
            time.sleep(0.5)  #Wait 0.5 seconds to give the player time to see the symbols, then hide them.
            buttons[previousX, previousY]['text'] = ' '
            buttons[x, y]['text'] = ' '
        else: #If the symbols match...
            buttons[previousX, previousY]['command'] = DISABLED #Disable the pair of matching buttons so the player can’t press them again.
            buttons[x, y]['command'] = DISABLED
        first = True #This line gets the function ready for the first button press of the next attempt.
            
    
    
            
root.mainloop()
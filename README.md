# python-games
games made with python

Different shapes appear on the screen at random in either black, red, green, or blue. If a color appears twice in succession, hit the snap key. Player 1 presses the “q” key to snap and player 2 the “p”
key. Each correct snap scores a point. Snap at the wrong time and you lose a point. The player with the highest score is the winner.

How it works
This project uses Tkinter to create the shapes. Tkinter’s mainloop() function schedules a function that you’ll create to show the next shape. The random module’s shuffle()
function makes sure the shapes always appear in a different order. The “q” and “p” keys are bound (linked) to a snap() function, so that each time one of these keys is pressed, it updates the relevant player’s score.

The program runs for as long as there are still shapes left to be revealed. It reacts to the key presses of the players when they
think they see a snap. When there are no more shapes left, the winner is declared and the game ends.

First import the random and time modules, and parts of Tkinter. Time lets you create a delay so that the player is able to read a
“SNAP!” or “WRONG!” message before the next shape is shown. HIDDEN lets you hide each shape until you want to show it with
NORMAL—otherwise all the shapes will appear on the screen at the start of the game.

The create.oval() function draws an oval as if it’s inside an invisible box. The four numbers within the brackets decide the position of the circles on the screen.
They are the coordinates of two opposing corners of the box. The greater the difference between the two pairs of numbers, the bigger the circle.

The bind() function tells the GUI to listen for the “q” or “p” key being pressed, and to call the snap() function each time it happens.

The focus_set() function tells the key presses to go to the canvas. The GUI wouldn’t react to “q” and “p” being pressed without this function being called.

A variable created in the main program, outside of a function, is called global and can be used in any part of the code. However, if you want to use a
function to assign a new value to a global variable, you need to add the keyword global before the variable’s name when you type it in the function.

The next_shape() function shows the colored shapes one after another, like cards being dealt.

To show a new shape, we need to change its state from HIDDEN to NORMAL by using Canvas’s itemconfigure() function.It uses another Canvas function, itemcget(), to update the
current_color variable, which will be used to check for a snap

c.delete(shape)
Deletes the current shape, so that the next shape doesn’t show on top of it and so that it won’t be shown again.

You can alter things that appear on the canvas by using Canvas’s itemconfigure() function. In this game, for instance, you use itemconfigure()
to change shapes from hidden to visible, but you could also use it to change their color or other characteristics. To use itemconfigure(), put the
name of the item you want to change in brackets, followed by a comma and then the characteristic and its new value.

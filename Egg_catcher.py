import itertools #to cycle through some colors
import random
from tkinter import Canvas, messagebox,font,Tk

canvas_width = 800
canvas_height = 600

root = Tk()#Creates a window
c = Canvas(root, width = canvas_width, height = canvas_height, background = 'deep sky blue')
c.create_rectangle(-5,canvas_height - 100, canvas_width * 5, canvas_height + 5, fill = 'sea green', width = 0) #creates the grass.
c.create_oval(-80, -80, 120, 120, fill = 'orange', width = 0) #creates the sun.
c.pack()

color_cycle = itertools.cycle(['light blue', 'light green', 'light pink', 'light yellow', 'light cyan']) #The cycle() function allows you to use each color in turn.
egg_width = 45
egg_height = 55
egg_score = 10 #Your score for catching an egg
egg_speed = 500
egg_interval = 4000 #A new egg appears every 4 seconds
difficulty_factor = 0.95 #This is how much the speed and interval change after each catch (closer to 1 is easier).

catcher_color = 'blue'
catcher_width = 100
catcher_height = 100 #This is the height of the circle that is used to draw the arc.
#These lines make the catcher start near the bottom of the canvas, in the center of the window.
catcher_start_x = canvas_width / 2 - catcher_width / 2 
catcher_start_y = canvas_height - catcher_height - 20
catcher_start_x2 = catcher_start_x + catcher_width
catcher_start_y2 = catcher_start_y + catcher_height

catcher = c.create_arc(catcher_start_x, catcher_start_y, catcher_start_x2, catcher_start_y2, \
    start = 200, extent = 140, style = 'arc', outline = catcher_color, width  = 3) #Start drawing at 200 degrees on the circle
#Draw for 140 degrees.The create_arc() function has two parameters, both given in degrees (°), that say where in the
#circle to draw the arc: start says where to start drawing, while extent is how many degrees to draw before stopping.
#Draw the catcher.

game_font = font.nametofont('TkFixedFont') #This line selects a cool computer-style font.
game_font.configure(size = 18)#You can make the text larger or smaller by changing this number.

score = 0
score_text = c.create_text(10, 10, anchor = 'nw', font = game_font, fill = 'dark blue', text = 'Score: ' + str(score))

lives_remaining = 3
lives_text = c.create_text(canvas_width - 10, 10, anchor = 'ne', fill = 'dark blue', font = game_font, text = 'Lives: ' + str(lives_remaining))

eggs = []#This is a list to keep track of the eggs.
def create_egg():
    x = random.randrange(10, 740) #Pick a random position along the top of the canvas for the new egg.
    y = 40
    new_egg = c.create_oval(x, y, x + egg_width, y + egg_height, fill = next(color_cycle), width = 0)
    eggs.append(new_egg) #The shape is added to the list of eggs.
    root.after(egg_interval, create_egg)#Call this function again after the number of milliseconds stored in egg_interval.
    
def move_eggs():
    for egg in eggs:
        (egg_x, egg_y, egg_x2, egg_y2) = c.coords(egg) #This line gets each egg’s coordinates.
        c.move(egg, 0, 10) #The egg drops down the screen 10 pixels at a time.
        if egg_y2 > canvas_height: #Is the egg at the bottom of the screen?
            egg_dropped(egg) #If so, call the function that deals with dropped eggs.
    root.after(egg_speed, move_eggs)
    
def egg_dropped(egg):
    eggs.remove(egg)
    c.delete(egg)
    lose_a_life()
    if lives_remaining == 0:
        messagebox.showinfo('GameOver!', 'Final Score: ' + str(score))
        root.destroy()
        
def lose_a_life():
    global lives_remaining
    lives_remaining -= 1
    c.itemconfigure(lives_text, text = 'Lives: ' + str(lives_remaining))
    
    
def check_catch():
    (catcher_x, catcher_y, catcher_x2, catcher_y2) = c.coords() #Get the coordinates of the catcher.
    for egg in eggs:
        (egg_x, egg_y, egg_x2, egg_y2) = c.coords()
        if catcher_x < egg_x and egg_x2 < catcher_x2 and catcher_y2 - egg_y2 < 40: #Is the egg inside the catcher horizontally and vertically?
            eggs.remove(egg)
            c.delete(egg)
            increase_score(egg_score)#Increase the score by 10 points
        root.after(100, check_catch)
        
def increase_score(points):
    global score, egg_speed, egg_interval
    score += points
    egg_speed = (egg_speed * difficulty_factor)
    egg_interval = (egg_interval * difficulty_factor)
    c.itemconfigure(score_text, text = 'Score: '+ str(score))
    
def move_left(event):
    (x1, y1, x2, y2) = c.coords(catcher)
    if x1 > 0:
        c.move(catcher, -20, 0)

def move_right(event):
    (x1, y1, x2, y2) = c.coords(catcher)
    if x2 < canvas_width:
        c.move(catcher, 20, 0)
        
c.bind('<Left>', move_left)
c.bind('<Right>', move_right)
c.focus_set()
    
root.after(1000, create_egg)
root.after(1000, move_eggs)
root.after(1000, check_catch) 
root.mainloop()
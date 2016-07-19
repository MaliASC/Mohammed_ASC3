from random import *

def setup():
    size(500,500)

x=randrange(500)
y=randrange(500)
xspeed = 5 
yspeed = 5
def draw():
    background(230,190,138)
    global x
    global y
    global xspeed
    global yspeed
    
    if x > 475 or x < 25:
        #change the x direction
        xspeed = xspeed * -1
    if y > 475 or y < 25:
        yspeed = yspeed * -1
    
        
    x += xspeed
    y += yspeed
    
    
    
    ellipse(x,y,50,50)
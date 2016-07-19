from random import *

def setup():
    size(500,500)

x=randrange(500)
y=randrange(500)
xspeed = 2 
yspeed = 2
def draw():
    background(230,190,138)
    global x
    global y
    global xspeed
    global yspeed
    
    if x > 475 or x < 25:
        #change the x direction
        xspeed = xspeed * -1
    if y < 25:
        yspeed = yspeed * -1
    
    if y >= 455:
         print(mouseX,x,mouseX+100)
         if x > mouseX and x < mouseX+100:
            yspeed = yspeed * -1
    
    x += xspeed
    y += yspeed
    ellipse(x,y,50,50)
    fill(0,0,0)
    
    paddle = rect(mouseX, 480, 100, 10)
    fill(255,0,0)
 


    
    

    
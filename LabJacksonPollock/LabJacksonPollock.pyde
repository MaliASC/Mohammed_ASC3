from random import *
def setup():
    size(400,400)
    
    
def draw():
    rect(randrange(400),randrange(400),randrange(1,50),randrange(1,50))
    ellipse(randrange(400),randrange(400),randrange(1,50),randrange(1,50))
    quad(randrange(400),randrange(400),randrange(1,50),randrange(1,50),randrange(400),randrange(400),randrange(1,50),randrange(1,50))
    fill(randrange(255),randrange(255),randrange(255))
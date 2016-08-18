pickColor = color(0, 0, 0)

def setup():
    size(400,400)

def draw():
    global pickColor
    fill(255,0,0)
    rect(0,0,50,50)
    fill(0,255,0)
    rect(50,0,50,50)
    fill(0,0,255)
    rect(100,0,50,50)
    fill(255,255,0)
    rect(150,0,50,50)
    fill(255,192,203)
    rect(200,0,50,50)
    fill(0,128,128)
    rect(250,0,50,50)
    fill(255,255,255)
    rect(300,0,50,50)
    fill(0,0,0)
    rect(350,0,50,50)
    
    if mouseButton == LEFT:
        if mouseY < 50:
          if mouseX < 50:
            pickColor = 1 #color(255, 0, 0)
      '''  else:
            fill(255, 0, 0)#(pickColor)
            ellipse(mouseX,mouseY,10,10)
    '''
    if mouseButton == LEFT:
        if mouseY  > 100:
          if mouseX > 50 and mouseX < 100:
            pickColor = color(0, 255, 0)
        else:
            fill(pickColor)
            ellipse(mouseX,mouseY,10,10)
    if mouseButton == LEFT:
        if mouseY > 150:
          if mouseX < 100:
            pickColor = color(0, 0, 255)
        else:
            fill(pickColor)
            ellipse(mouseX,mouseY,10,10)
    if mouseButton == LEFT:
        if mouseY  > 200:
          if mouseX < 150:
            pickColor = color(255, 255, 0)
        else:
            fill(pickColor)
            ellipse(mouseX,mouseY,10,10)
        if mouseButton == LEFT:
            if mouseY < 250:
                if mouseX < 200:
                    pickColor = color(255,192,203)
        else:
            fill(pickColor)
            ellipse(mouseX,mouseY,10,10)
    if mouseButton == LEFT:
        if mouseY  > 300:
          if mouseX < 250:
            pickColor = color(0,128,128)
        else:
            fill(pickColor)
            ellipse(mouseX,mouseY,10,10)
    if mouseButton == LEFT:
        if mouseY > 350:
          if mouseX < 300:
            pickColor = color(255,255,255)
        else:
            fill(pickColor)
            ellipse(mouseX,mouseY,10,10)
    if mouseButton == LEFT:
        if mouseY > 400:
          if mouseX < 350:
            pickColor = color(0,0,0)
        else:
            fill(pickColor)
            ellipse(mouseX,mouseY,10,10)

    
    
  
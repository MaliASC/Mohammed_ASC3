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
    fill(225,225,225)
    rect(300,0,50,50)
    fill(0,0,0)
    rect(350,0,50,50)
    
    if mouseButton == LEFT:#check if they ever clicked on the screen
        
        #check if you are in the color pannel and what color pannel you picked
        if mouseY < 50 and mouseX < 50:
            pickColor = 1 #color(255, 0, 0)
        elif mouseY < 50 and mouseX > 50 and mouseX < 100:
             pickColor = 2 #color(0, 255, 0)
        elif mouseY < 50 and mouseX > 100 and mouseX < 150:
             pickColor = 3 #color(0, 0, 255)
        elif mouseY < 50 and mouseX > 150 and mouseX < 200:
             pickColor = 4 #color(255, 225, 0)
        elif mouseY < 50 and mouseX > 200 and mouseX < 250:
             pickColor = 5 #color(255,192,203)
        elif mouseY < 50 and mouseX > 250 and mouseX < 300:
             pickColor = 6 #color(0,128,128)
        elif mouseY < 50 and mouseX > 300 and mouseX < 350:
             pickColor = 7 #color(255, 255, 255)
        elif mouseY < 50 and mouseX > 400 and mouseX < 450:
             pickColor = 8 #color(0,0,0)
             
        #check if you are in the drawing area and draw using the appropriate color
        
        if mouseY >50 and pickColor ==1: #that means you are in the drawing area
            fill(255,0,0)
        elif mouseY >50 and pickColor ==2: #that means you are in the drawing area
            fill(0,255,0)   
        elif mouseY >50 and pickColor ==3: #that means you are in the drawing area
            fill(0,0,255)  
        elif mouseY >50 and pickColor ==4: #that means you are in the drawing area
            fill(255,255,0)   
        elif mouseY >50 and pickColor ==5: #that means you are in the drawing area
            fill(255,192,203)  
        elif mouseY >50 and pickColor ==6: #that means you are in the drawing area
            fill(0,128,128)  
        elif mouseY >50 and pickColor ==7: #that means you are in the drawing area
            fill(255,255,255)   
        elif mouseY >50 and pickColor ==8: #that means you are in the drawing area
            fill(0,0,0)         
        ellipse(mouseX,mouseY,10,10)
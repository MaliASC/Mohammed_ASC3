#Space Invaders! Early Beta Version
fieldX = 25                           #x and coordinate of grid
fieldY = 50         
fieldXSpeed = 1                       #sets translation speed of field
fieldYSpeed = 10
alienXspeed = 1                                 #alien's horizontal speed 
alienGrid = [[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]]           #stores alive/death status of aliens (1=alive, 0=dead)
blockGrid = []                                       #blocks are just static aliens!    
shipXcoord = 200                                    #ship's x coordinates
ship_speed = 10                                     #ship's horizontal speed
laserX = 200                                       #laser's x and y coordinates  
laserY = 415                  
shot = False                               #determiens if laser was shot or not
score = 0                                          #ship score
windowLength = 500                              #length of game window (in pixels)
print(alienGrid)
print(blockGrid)
def setup():
    size(windowLength,windowLength)
def draw():
    global fieldX, fieldY, fieldXSpeed, fieldYSpeed, alienGrid, shipXcoord, laserX, laserY, shot, score
    background (0)
    fill(255,0,0)     
    rect(shipXcoord,415,30,30)                         #make ship
    if shot == True:                                 #fires bullet if shot
        fill(0,255,0) 
        rect(laserX,laserY,5,20)                            #creates laser
        laserY -= 20                                        #translates laser
        if laserY < 0:                                         #resets laser after hitting top-boundary
            shot = False 
            laserY = 415                                                             
    for i in range(len(alienGrid)):                       #draws aliens (i for groups/columns, y for rows)
        for y in range(len(alienGrid[i])):              #-6 to control the amount of rows (we want it to be five here)
            if alienGrid[i][y]==1: 
                if i*35+fieldX-10<=laserX<=i*35+fieldX+20 and laserY<=y*30+fieldY+20: #checks if laser lands between the bottom vertices of alien (-10 so that the right corner of laser collides)
                    alienGrid[i][y]=0                              #marks alien as 0/dead
                    shot = False                              #resets laser  (or it would become a canon!)
                    laserY = 415
                    score +=100
                else:
                    fill(255,0,0)             
                    rect(i*35+fieldX,y*30+fieldY,20,20)        #creates our alien (i/y* # seperates each column/row by that many pixels)
    if fieldX<25 or fieldX>105:                #assigns boundary to grid 
        fieldXSpeed*=-1                    
        fieldY +=fieldYSpeed
    fieldX += fieldXSpeed
    textSize(30)                                #prints score up top
    text("Score: ", 180, 25)
    text(str(score),275, 25)
    frameRate(60)
def keyPressed():   #movement of ship
    global shot, shipXcoord, laserX, laserY, ship_speed 
    if keyCode == RIGHT and shipXcoord < 470:
        shipXcoord += ship_speed
    if keyCode == LEFT and shipXcoord > 0:              
        shipXcoord -= ship_speed 
    if keyCode == 32:
        laserX = shipXcoord
        shot = True
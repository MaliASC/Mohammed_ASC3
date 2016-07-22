#Space Invaders! Early Beta Version
#REPLICE GRID[i][0] WITH ALIENXCOORD SOMEhow. More variables/less hardcoding!
alienXcoord = 0          #left/top boundary of aliens and way to translate and detect collision
alienYcoord = 0
alienXspeed = 1              #alien's horizontal speed 
alienGrid = []               #grid used to create/store aliens
blockXcoord = 50           #starting x coord of blocks)
blockYcoord = 0
for i in range(5):           #creates x and y cooridinates of aliens (i specifies amount of columns, y for rows)
    for y in range(3):
        alienGrid.append([25+i*75,50+y*75])       #(i/y*number seperates the columns and rows(the specific distance is number-50 (or side length))
blockGrid = []                    #blocks are just static aliens! 
for i in range(5):                #creates blocks (takes x coordinates) 
        blockGrid.append(i*75)   
shipXcoord = 200                 #ship's x coordinates
laserX = 0
laserY = 415                  #laser's y coordinates  
shot = False            #determiens if laser was shot or not
windowLength = 500           #length of game window (in pixels)
print(alienGrid)
print(blockGrid)
def setup():
    size(windowLength,windowLength)
def draw():
    global alienXcoord
    global alienYcoord
    global alienXspeed
    global alienGrid
    global blockXcoord
    global blockGrid
    global shipXcoord
    global laserX
    global laserY
    global shot
    background (0)
    fill(255,0,0)     
    rect(shipXcoord,415,30,30)  #make ship
    if shot == True:              #fires bullet if shot
        fill(0,255,0)
        ellipse(laserX,laserY,30,30)
        laserY -= 20
        if laserY < 0:
            shot = False 
            laserY = 415                                                             
    for i in range(len(alienGrid)):    #draws aliens 
        fill(255,0,0)
        rect(alienGrid[i][0],alienGrid[i][1],50,50)
    # for i in range(len(blockGrid)):    #draws blocks
    #         # noStroke()
    #         fill(255,0,0)
    #         rect(blockGrid[i]+blockXcoord,400,50,50)    
    alienXcoord += alienXspeed         #for boundary stuff
    for i in range(len(alienGrid)):
        alienGrid[i][0]+=alienXcoord
        alienGrid[i][1]+=alienYcoord
    # for i in range (len(alienGrid)):
    # alienGrid[i][0] += alienXcoord
    # alienGrid[i][1] += alienYcoord
    if alienXcoord<0 or alienXcoord>windowLength-400:          #checks if alien is within boundaries
        alienXspeed = alienXspeed*-1                          #if out of bounds, the alien will reverse its dirction and move down slightly) 
        alienYcoord +=25
        
    for i in range(len(alienGrid)):  
        try: 
            if alienGrid[i][0]+alienXcoord<=laserX<=alienGrid[i][0]+alienXcoord+50 and laserY==alienGrid[i][1]+alienYcoord+75:     #checking each alien if laser is inbetween the bottom vertices(bottom side) of alien and at the same y coord
                del alienGrid[i]             #removes object from list/stored memory  
        except:
            pass
    # for i in range(len(blockGrid)):    
    #     try: 
    #         if blockGrid[i][0]<=laserX<=blockGrid[i][0]+50 and laserY==blockGrid[i][1]+50:     #checking each alien if laser is inbetween the bottom vertices(bottom side) of alien and at the same y coord
    #             del blockGrid[i]             #removes object from list/stored memory  
    #     except:
    #         pass    
    print(alienGrid)
    print(blockGrid)
    frameRate(20)
def keyPressed():   #movement of ship
    global shot
    global shipXcoord
    global laserX
    global laserY
    if keyCode == RIGHT and shipXcoord < 480 :
        shipXcoord += 5
    if keyCode == LEFT and shipXcoord > 0:              
        shipXcoord -= 5    
    if keyCode == 32:
        laserX = shipXcoord
        shot = True
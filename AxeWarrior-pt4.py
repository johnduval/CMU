#############################
###                       ###
### AXE WARRIOR - PART 1  ###
###                       ###
#############################

# Create global variables.
# Modify initializeGame (taken from tic-tac-toe)
# Create player's starting Hit Points (HP) in initializeGame()
# Create player movement (bounded motion)
    # Use arrows.
# Obstacles
    # Unable to cross Mountains
    
    
#############################
###                       ###
### AXE WARRIOR - PART 2  ###
###                       ###
#############################

# Gain / Loose HP from stepping on to fire & life squres.
    # Print Starting HP to Console
    # When gaining or loosing health: Print info to console
        # Starting Health
        # Ending Health
        # Amount health gained / losed.
# Randomize the squares.
    # Print total number of squares to the Console.
    

#############################
###                       ###
### AXE WARRIOR - PART 3  ###
###                       ###
#############################

# Movement through portals
# Enemies on screen
# Move enemy with 'wasd'

#############################
###                       ###
### AXE WARRIOR - PART 4  ###
###                       ###
#############################

# Randomize enemy Movement
# Warrior has Bounded Motion.
# Enemy connot go through obstacles (Mountain, Life, or Fire)
# Enemy can take portals.
# Create a battle screen when Enemy & Warrior are on top of each other.


app.rows = 9
app.cols = 10
app.board = makeList(app.rows, app.cols)
board = Group()
# Distance objects move in game (also same as each cell size)
app.movement = 0

fireSquares = Group ()
lifeSquares = Group ()
mountainSquares = Group ()
portals = Group ()
# Store player's hit points.
app.hitPoints = [ ]
app.heartUrl = 'https://pm1.narvii.com/6696/35ce165bcb7637f41c7597fc6761479655aa0c98_hq.jpg'
app.warriorUrl = 'https://a.wattpad.com/useravatar/Sunpool.256.143085.jpg'
app.enemyUrl = 'https://www1.cbn.com/sites/default/files/styles/image_xl_640x480/public/evil_character_devil_si.jpg'


def initializeGame():
    # Create the board and initialize game properties.
    cellSize = 400 / 10
    # Lets us know how far objects should move in 1 turn.
    app.movement = cellSize
    for row in range(app.rows):
        for col in range(app.cols):
            x = col * cellSize
            y = row * cellSize
            board.add(
                Rect(x, y, cellSize, cellSize, fill='skyBlue',
                     border='lightCyan', borderWidth=1)
                )
            # Sets up squares as blanks.
            app.board [row][col] = False

    app.warrior = Image (app.warriorUrl,1,1,height=38,width=38)
    app.enemy = Image (app.enemyUrl, 361,321,height=38,width=38)

    HPs = 6
    for i in range (HPs):
        x = i * app.movement + 8
        app.hitPoints.append (Image (app.heartUrl, x,357))
        app.hitPoints[i].width = 23
        app.hitPoints[i].height = 26
        app.hitPoints[i].toBack()
    print ("Starting HP: " + str (len(app.hitPoints))) #PART 2
    app.isGamePlaying = False

initializeGame()

# PART 2
def drawHearts (hpChange):
    print ("Starting HP: " + str (len(app.hitPoints)))
    if (hpChange < 0):
        for i in range (abs(hpChange)):
            hp = len (app.hitPoints)
            # print (hp)
            if (hp <= 1):
                gameOver()
            if (hp >= 1):
                app.hitPoints[hp-1].visible = False
                app.hitPoints.pop()
    if (hpChange > 0):
        for i in range (abs (hpChange)):
            hp = len (app.hitPoints)
            app.hitPoints.append (Image (app.heartUrl, hp * app.movement + 8,357))
            app.hitPoints[hp].width /= 40
            app.hitPoints[hp].height /= 40
            app.hitPoints[hp].toBack()
        target = lifeSquares.hitTest(app.warrior.centerX, app.warrior.centerY)
        lifeSquares.remove(target)
    print ("Ending HP: " + str (len(app.hitPoints))) 
    print ("You HP changed by: " + str (hpChange))


def groupLength (g):
    counter = 0
    for i in g.children:
        counter += 1
    return counter
    

#Draws area on map our player cannot pass, OR cause damage!
def drawObstacles ():
    # have 10 'x' tiles across, 9 'y' down.
    # Randomize if a mountain (cannot move over!) or flame (lose 1 HP!)
    number_ms = randrange (1,6)
    print ("Mountain #: " + str (number_ms))
    while (number_ms != groupLength (mountainSquares)):
        # Starts at 1 so we don't start on Warrior.
        x = randrange (1,9)
        y = randrange (1,8)
        if (app.board[y][x] == False):
            mountainSquares.add (Rect (x*app.movement,y*app.movement,app.movement,app.movement,fill='grey'))
            app.board [y][x] = True
    number_fs = randrange (2,5)
    print ("Fire #: " + str (number_fs))
    while (number_fs != groupLength (fireSquares)):
        x = randrange (1,9)
        y = randrange (1,8)
        if (app.board[y][x] == False):
            fireSquares.add (Rect (x*app.movement,y*app.movement,app.movement,app.movement,fill='red'))
            app.board [y][x] = True
    
    number_ls = randrange (1,9)
    print ("Life #: " + str (number_ls))
    while (number_ls != groupLength (lifeSquares)):
        x = randrange (1,9)
        y = randrange (1,8)
        if (app.board[y][x] == False):
            lifeSquares.add (Rect (x*app.movement,y*app.movement,app.movement,app.movement,fill='green'))
            app.board [y][x] = True
    
    # Part 3!
    portal1 = Circle (20,180,app.movement/2,fill='orange')
    portal2 = Circle (380,180,app.movement/2,fill = 'orange')
    portal3 = Circle (220,20,app.movement/2,fill='blue')
    portal4 = Circle (220,340,app.movement/2,fill = 'blue')
    portals.add (portal1)
    portals.add (portal2)
    portals.add (portal3) 
    portals.add (portal4)
    
drawObstacles()

# Defines gameOver and newGame screens.
newGameScreen = Group(
    Rect(0, 100, 400, 200, fill='aliceBlue', opacity=70),
    Label('Welcome to Axe Warrior!', 200, 190, fill='darkOrange', size=30,
          bold=True),
    Label('press space to start a new game', 200, 220, fill='darkOrange',
          size=15, bold=True)
    )
    
# Draws and setss gameOverScreen.
gameOverScreen = Group (
    Rect(0, 100, 400, 200, fill='orange', opacity=60),
    Label ("0 HIT POINTS.  GAME OVER  :(",200,200,size=20)
    )
gameOverScreen.visible = False

def gameOver():
    gameOverScreen.visible = True
    app.stop()
    

# PART 4 - this is screen that will appear when Warrior & Enemy Battle
# (happens when their centerX & centerY are equal)

battleScreen = Group(
    ??????? (your own code here for a battle screen - may be similar to newGameScreen & gameOverScreen)
    )
# make sure battleScreen is not visible to start.
battleScreen.visible = ...

# Do nothing inside battle() currently.  Coding a Battle will be part 5
def battle ():
    pass



# Part 3 - moved into its own def.
# ALSO now checking for portals!
def checkObstaclesWarrior (key, warriorCurrentPos):
    if (app.warrior.hitsShape (fireSquares) == True):
        drawHearts (-1)
    if (app.warrior.hitsShape (lifeSquares) == True):
        drawHearts (2)
    if (app.warrior.hitsShape (mountainSquares) == True):
        app.warrior.centerX = warriorCurrentPos[0]
        app.warrior.centerY = warriorCurrentPos[1]
    

def checkPortalWarrior (key, warriorCurrentPos):
    if (app.warrior.hitsShape (portals) == True):
        if (app.warrior.centerX == 20):
            app.warrior.centerX = 380
        elif (app.warrior.centerX == 380):
            app.warrior.centerX = 20
        elif (app.warrior.centerY == 20):
            app.warrior.centerY = 340
        elif (app.warrior.centerY == 340):
            app.warrior.centerY = 20
        
# Part 3 - moved into its own def.
def moveWarrior (key, warriorCurrentPos):
    if (key == 'right'):
        app.warrior.centerX += app.movement
    if (key == 'left'):
        app.warrior.centerX -= app.movement
    if (key == 'up'):
        app.warrior.centerY -= app.movement
    if (key == 'down'):
        app.warrior.centerY += app.movement
    if (app.warrior.centerX > 400 or app.warrior.centerX < 0 or app.warrior.centerY > 400-app.movement or app.warrior.centerY < 0):
        app.warrior.centerX = warriorCurrentPos[0]
        app.warrior.centerY = warriorCurrentPos[1]
        
    checkObstaclesWarrior (key, warriorCurrentPos)
    checkPortalWarrior (key, warriorCurrentPos)

# PART 4 - Enemy Movement.
    
def checkObstacleEnemey (key, enemyCurrentPos):
    # Code is just like checking if Warrior hits an obstacle.
    # Only in this case - Enemy should not be able to move if it hitsShape of...
    # fireSquare, lifeSquare, OR mountainSquare
    if (???):
        # Set enemy movement to enemyCurrentPos (just like if Warrior hits a mountainSquare)
        ???
        ???
        
def checkPortalEnemy (key, enemyCurrentPos):
    # Enemy can move through portals!!!
    # Did enemy hitsShape portals?
    IF so... update location.
    if (???):
        if (app.enemy.centerX == 20):
            app.enemy.centerX = ...
        elif (app.enemy.centerX ......):
            ???
        elif (???):
            ???
        elif (???):
            ???

    # PART 4 - NOW RANDOMIZED
def moveEnemy (key, enemyCurrentPos):
    # Randomize your x & y.
    # -1 = move left / up
    # 0 = do not move
    # 1 = move right / down
    xMove = ...
    yMove = ...
    # Next 4 lines are simply for troubleshooting code.
    print (app.warrior.centerX)
    print (app.enemy.centerX)
    print (app.warrior.centerY)
    print (app.enemy.centerY)
    # Check to see if app.warriors centerX & centerY values are equal to each other (USE A COMPOUND IF)
    # IF so, set xMove & yMove to 0.
    # This prevents the Enemy from moving if Warrior lands on top of Enemy.
    if (app.warrior.centerX == app.enemy.centerX and .......):
        print ("ENEMY SHOULD NOT MOVE")
        xMove = ...
        ????
    # multiple yMove & xMove by app.movement.  This will make them move a whole square.
    xMove *= ...
    ???
    # Next 2 lines: Actually move the Enemy by center its new centerX & center Y based on xMove & yMove
    ???
    ???
    # IF - Bounded motion check to make sure Enemy isn't outside the arena.  Exact same concept as checking your Warrior.
    if (?....):
        ???
        ???
    # Now going to check if Enemy Hits an Obstacle
    checkObstacleEnemey (key, enemyCurrentPos)
    # Check if Enemy hits a Portal.
    checkPortalEnemy (key, enemyCurrentPos)

    

def onKeyPress(key):
    # Start a new game or restart the game.
    # When space is pressed and the game is not already playing,
    # make the newGameScreen invisible and set isGamePlaying.
    ### Place Your Code Here ###
    
    # Storing player's current position.
    # This allows us to move player back to original position if goes out of bounds OR hits an object.
    # Part 3 = moved here.
    warriorCurrentPos = [app.warrior.centerX, app.warrior.centerY]
    enemyCurrentPos = [app.enemy.centerX, app.enemy.centerY]

    
    if (key == 'space'):
        if (app.isGamePlaying == False):
            app.isGamePlaying = True
            newGameScreen.visible = False
    # Only tries moving if isGamePlaying is True!
    if (app.isGamePlaying == True):
        # Part 3 - moved into its own def. - move warrior in based arrow direction.
        moveWarrior (key, warriorCurrentPos)
        # Part 4 - ENemy movement!
        moveEnemy (key, enemyCurrentPos)
        # Check if app.warrior centerX & centerY is equal to the app.enemy
        # (hint: same logic that applies when checking if enemy xMove & yMove is set to 0)
        if (????):
            # Make battleScreen visible
            battleScreen.visible = ...
            # Call battle function
            ???
            print ("WHOA")  #Troubleshooting code to see if make it into this IF block.
        else:
            battleScreen.visible = False
        
            
def onMousePress (x,y):
    print (len(app.hitPoints))

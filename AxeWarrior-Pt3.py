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




app.rows = 9
app.cols = 10
app.board = makeList(app.rows, app.cols)
board = Group()
# Distance objects move in game (also same as each cell size)
app.movement = 0

fireSquares = Group ()
lifeSquares = Group ()
mountainSquares = Group ()
# NEW - PART 4
portals = Group ()

# Store player's hit points.
app.hitPoints = [ ]
app.heartUrl = 'https://pm1.narvii.com/6696/35ce165bcb7637f41c7597fc6761479655aa0c98_hq.jpg'
app.warriorUrl = 'https://a.wattpad.com/useravatar/Sunpool.256.143085.jpg'

# Link for enemy icon
app.enemyUrl = ...


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
    # Create your enemy on the screen - start him away from your Warrior.
    app.enemy = ....

    HPs = 6
    for i in range (HPs):
        x = i * app.movement + 8
        app.hitPoints.append (Image (app.heartUrl, x,357))
        app.hitPoints[i].width = 23
        app.hitPoints[i].height = 26
        app.hitPoints[i].toBack()
    print ("Starting HP: " + str (len(app.hitPoints)))
    app.isGamePlaying = False

initializeGame()

def drawHearts (hpChange):
    print ("Starting HP: " + str (len(app.hitPoints)))
    if (hpChange < 0):
        for i in range (abs(hpChange)):
            hp = len (app.hitPoints)
            # print (hp)
            if (hp <= 1):
                # Label ("0 HIT POINTS.  GAME OVER  :(",200,200,size=20)
                # print ("END")
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
        # print ("YAY " + str(len(app.hitPoints)))
        target = lifeSquares.hitTest(app.warrior.centerX, app.warrior.centerY)
        # print (target)
        lifeSquares.remove(target)
    print ("Ending HP: " + str (len(app.hitPoints))) 
    print ("You HP changed by: " + str (hpChange))


def groupLength (g):
    counter = 0
    for i in g.children:
        counter += 1
    return counter

# PART 3 INSIDE FUNCTION.
#Draws area on map our player cannot pass, OR cause damage!
def drawObstacles ():
    # have 10 'x' tiles across, 9 'y' down.
    # Randomize if a mountain (cannot move over!) or flame (lose 1 HP!)
    number_ms = randrange (1,6)
    print ("Mountain #: " + str (number_ms))
    while (number_ms != groupLength (mountainSquares)):
        # Starts at 1 so we don't start on Warrior.
        x = randrange (1,10)
        y = randrange (1,9)
        if (app.board[y][x] == False):
            mountainSquares.add (Rect (x*app.movement,y*app.movement,app.movement,app.movement,fill='grey'))
            app.board [y][x] = True
    number_fs = randrange (2,5)
    print ("Fire #: " + str (number_fs))
    while (number_fs != groupLength (fireSquares)):
        x = randrange (1,10)
        y = randrange (1,9)
        if (app.board[y][x] == False):
            fireSquares.add (Rect (x*app.movement,y*app.movement,app.movement,app.movement,fill='red'))
            app.board [y][x] = True
    

    number_ls = randrange (1,9)
    print ("Life #: " + str (number_ls))
    while (number_ls != groupLength (lifeSquares)):
        x = randrange (1,10)
        y = randrange (1,9)
        if (app.board[y][x] == False):
            lifeSquares.add (Rect (x*app.movement,y*app.movement,app.movement,app.movement,fill='green'))
            app.board [y][x] = True
    
    # Part 3!
    # Draw 4 portals - refer to example canavas for the Circles.
    portal1 = Circle (20,180,app.movement/2,fill='orange')    # Draw your other 3 portals
    ...
    ...
    ...
    # Add the 4 portals to portals Group
    portals.????
    ...
    ...
    ...
    ...
    
    
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

######
# PART 3 - MOVED WARRIOR MOVEMENTS ITO THEIR OWN FUNCTIONS
######


# Part 3 - moved checking obstacles into its own def.
# ALSO now checking for portals!
def checkObstaclesWarrior (key, warriorCurrentPos):
    # Perform your checks on hitting fire, life, and mountain squares here.
    # The code doesn't really change - it's just in a different loction now.
    
    
# Checks for portals.
def checkPortalWarrior (key, warriorCurrentPos):
    if (app.warrior.hitsShape (portals) == True):
        if (app.warrior.centerX == 20):
            app.warrior.centerX = 380
        elif (app.warrior.centerX == 380):
            app.warrior.centerX = 20
        # Now do the same thing, but only accounting for your warrior hitting the ther two portals
        # Hitting top-most portal will move to bottom-most portal, and other way around.
        elif ...
            ...
        elif ...
            ...
        
# Part 3 - moved Warrior Movement (bounded) into its own def.
# Move your warrior using bounded motion - just like before.
# Yes, copy and paste your code!
def moveWarrior (key, warriorCurrentPos):
    # Bounded Motion Code
    .............


    
    # TWO NEW LINES:
    # Call two functions to check for obstacles and portals
    checkObstaclesWarrior (key, warriorCurrentPos)
    .... # Call the Portal Function - be sure to check your parameter.
    

# Will be coded Part 4
def checkObstacleEnemey (key, enemyCurrentPos):
    pass

# Will be coded Part 4.
def checkPortalEnemy (key, enemyCurrentPos):
    pass
   


# Move your Enemey with 'wasd'
    # Use bounded motion.
    # Don't worry about hitting obstacles or portals yet.
def moveEnemy (key, enemyCurrentPos):
    
    
    # Bounded Motion Code
    .............
    
    # These two lines remain as last 2 in def moveEnemy (key, enemyCurrentPos)
    checkObstacleEnemey (key, enemyCurrentPos)
    checkPortalEnemy (key, enemyCurrentPos)

    

def onKeyPress(key):
    # Part 3 - these lines moved / added here
    warriorCurrentPos = [app.warrior.centerX, app.warrior.centerY]
    enemyCurrentPos = [app.enemy.centerX, app.enemy.centerY]

    if (key == 'space'):
        if (app.isGamePlaying == False):
            app.isGamePlaying = True
            newGameScreen.visible = False
    # Only tries moving if isGamePlaying is True!
    if (app.isGamePlaying == True):
        # Part 3 - moved Warrior movment + checking Life, Fire, & Mountain Squares to its own function.
        # ALSO adding check for portals now!!!
        moveWarrior (key, warriorCurrentPos)
        # Add call to function that moves the enemy...
        ...
        
       
            
def onMousePress (x,y):
    print (len(app.hitPoints))

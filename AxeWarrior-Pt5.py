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

# Randomize enemy Movement whenever Warrior moves.
# Warrior has Bounded Motion.
# Enemy connot go through obstacles (Mountain, Life, or Fire)
# Enemy can take portals.
# Create a battle screen when Enemy & Warrior are on top of each other.

#############################
###                       ###
### AXE WARRIOR - PART 5  ###
###                       ###
#############################

# When Warrior is on top of Enemy, start the battle screen!
    # Use a key as a shortcut to move Warrior on top of Enemy.
# Display relevant data.
# Hit a key or click mouse for warrior to attack.
# If HP for warrior or enemy drops below 0, show a screen telling as much.


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
# Part 5
# Boolean to see if battle has started - set to False
app.battleStarted = ...

# Enemy's max HP

app.enemyHpMax = ...

# Stats for fight - set to 0 to start.  Will randomize later.
app.warriorAtk = ...
app.enemyAtk = ...
app.warriorDef = ...
app.enemyDef = ...

# MAX Value for stats from above - will used to randomize later.
app.warriorAtkMAX = 8
app.enemyAtkMAX = ...
app.warriorDefMAX = ...
app.enemyDefMAX = ...

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
# Part 5 addition - prevents error when counting HP durig a battle.
        if (target != None):
            lifeSquares.remove(target)
    print ("Ending HP: " + str (len(app.hitPoints))) 
    print ("You HP changed by: " + str (hpChange))


def groupLength (g):
    counter = 0
    for i in g.children:
        counter += 1
    return counter
    

# PART 2: ADD RANDOMIZATION.
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
    Rect(0, 100, 400, 200, fill='orange', opacity=70),
    Label ("0 HIT POINTS.  GAME OVER  :(",200,200,size=20)
    )
gameOverScreen.visible = False

def gameOver():
    gameOverScreen.visible = True
    gameOverScreen.toFront()
    app.stop()


# Part 5
# Create an enemyDead Screen (meaning you won!)
enemeyDeadScreen = Group ()
# Set screen to False to start
enemeyDeadScreen.visible = ...


# Creates enemyDead function - call if we kill the enemy.
def enemyDead ():
    # Make the enemeyDeadScreen visible
    ???
    # Bring enemeyDeadScreen to the front
    ???
    # Stop the app
    ???
        
    
    
    
# Part 5
# Fill in Labels! (including the Presss..... to attack)
battleScreen = Group(
    Rect (0,0,400,400-app.movement,fill='grey', opacity = 75),
    Label (???, 200,50,size=50,fill='yellow',bold=True),
    Label(???, 100,100,size=25),
    Label(???, 300,100,size = 25),
    Label("Press ............. to Attack!",200,215,fill='blue',size=35)
    )

# Create an EMPTY battleScreenData Group
battleScreenData = ...
# Set battleScreen to not be visibsle
???
# Set battleScreenData to not be visibsle
???


# Part 5
# Create your battle function - be sure to include they key parameter
def battle (key):
    # Set player HP equal to the length of app.hitPoints.  To display current hp.
    playerHp = len (app.hitPoints)
    # Check IF app.battleStarted is False
    if (???):
        # Set to a random range from 1 to MAX value
        app.enemyHp= randrange (1,app.enemyHpMax)
        # Set to a random range from 0 to MAX value
        app.warriorAtk = randrange (0,app.warriorAtkMAX)
        # Set to a random range from 0 to MAX value
        app.warriorDef = randrange(...)
        # Set to a random range from 0 to MAX value
        app.enemyAtk = ...
        # Set to a random range from 0 to MAX value
        app.enemyDef = ...
        # Set app.battleStarted to True
        app.battleStarted = True
    # Back outside IF statement.
    # Clear battleScreenData
    battleScreenData.clear()
    # warriorHpLabel's value the player's current HP for the value (hint - look at first line in this function)
    warriorHpLabel = Label(...,130,125,size=20, fill = 'red')
    # Add Following Label to Warrior info:
    battleScreenData.add (warriorHpLabel)
    battleScreenData.add (Label("HP: ",100,125,size=20, fill = 'red'))
    # Finish next two lines
    battleScreenData.add (Label("Attack: " + str (app.warriorAtk),...)
    battleScreenData.add (Label.........)
    
    
    enemeyHpLabel = Label(app.enemyHp,330,125,size=20,fill = 'red')
    # Add Following Label to Enemy info:
    battleScreenData.add (enemeyHpLabel)
    battleScreenData.add (Label("HP: ",300,125,size=20, fill = 'red'))
    # Finish next 2 lines...
    battleScreenData.add (Label("Attack: " + str (app.enemyAtk),....))
    battleScreenData.add (Label.......)
    # Debugging Lines...
    # print (app.warriorAtk)
    # print (app.warriorDef)
    # print (app.enemyAtk)
    # print (app.enemyDef)
    # Check if key is equal to some value - this will be the same as the Label from your battleScreen Group
    if (?????):
        # Add Label to battleScreen indicating you've attached.
        ???
        # Check if app.enemyAtk is greater than app.warriorDef
        if (???):
            # Create a new variable calculating the HP loss for warrior.
            warriorDelta = ...
            print ("warrior change in HP: " + str (warriorDelta))
            # Call function that calculates Heart Change.
            drawHearts(warriorDelta)
            playerHp = len (app.hitPoints)
            warriorHpLabel.value=playerHp
        # Check if app.warriorAtk is greater than app.enemyDef
        if (????):
            # Create a new variable calculating the HP loss for enemy.
            ??? = ???
            # Subtract the loss in HP from app.enemyHp (hint: you just calculated this)
            app.enemyHp -= ...
            enemeyHpLabel.value = app.enemyHp
            # Check if app.enemyHp is less than or equal to 0...
            if (???):
                # Call enemyDead function if so...
                ???
            

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
# Part 5 - Added 'q'
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
# Part 5
# Moves warrior on top of enemy - Avoids having to move warrios / enemy over and over to troubleshoot
# Use for debugging the FightScreen
    if (key == 'q'):
        app.warrior.centerX = app.enemy.centerX
        app.warrior.centerY = app.enemy.centerY
        
    checkObstaclesWarrior (key, warriorCurrentPos)
    checkPortalWarrior (key, warriorCurrentPos)

# PART 4 - Enemy Movement.
    
def checkObstacleEnemey (key, enemyCurrentPos):
    if ((app.enemy.hitsShape (fireSquares) == True) or (app.enemy.hitsShape (lifeSquares) == True) or (app.enemy.hitsShape (mountainSquares) == True)):
        app.enemy.centerX = enemyCurrentPos[0]
        app.enemy.centerY = enemyCurrentPos[1]
        
def checkPortalEnemy (key, enemyCurrentPos):
    if (app.enemy.hitsShape (portals) == True):
        if (app.enemy.centerX == 20):
            app.enemy.centerX = 380
        elif (app.enemy.centerX == 380):
            app.enemy.centerX = 20
        elif (app.enemy.centerY == 20):
            app.enemy.centerY = 340
        elif (app.enemy.centerY == 340):
            app.enemy.centerY = 20
   
    
def moveEnemy (key, enemyCurrentPos):
    
    xMove = randrange (-1,2)
    yMove = randrange (-1,2)
    # Troubleshooting prints
    # print (app.warrior.centerX)
    # print (app.enemy.centerX)
    # print (app.warrior.centerY)
    # print (app.enemy.centerY)
    if (app.warrior.centerX == app.enemy.centerX and app.warrior.centerY == app.enemy.centerY):
        xMove = 0
        yMove = 0

    xMove *= app.movement
    yMove *= app.movement
    app.enemy.centerX+=xMove
    app.enemy.centerY+=yMove
    if (app.enemy.centerX > 400 or app.enemy.centerX < 0 or app.enemy.centerY > 400-app.movement or app.enemy.centerY < 0):
        app.enemy.centerX = enemyCurrentPos[0]
        app.enemy.centerY = enemyCurrentPos[1]
    checkObstacleEnemey (key, enemyCurrentPos)
    checkPortalEnemy (key, enemyCurrentPos)

    
# Added a couple lines for Part 5 below.
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
        # Part 5 - Adding an IF to check if battleScreen.visible is False.  If so, call moveWarrior & moveEnemy
        if (battleScreen.visible == False):
            moveWarrior (key, warriorCurrentPos)
            moveEnemy (key, enemyCurrentPos)
        # Part 3 - moved checking Life, Fire, & Mountain Squares to its own function.
        # ALSO adding check for portals now!!!
        if (app.warrior.centerX == app.enemy.centerX and app.warrior.centerY == app.enemy.centerY):
# Part 5 added.
            # Set battleScreen visisble to True
            ???
            # Set battleScreenData visible to True
            ???
            # part 5 = added parameter key
            battle(key)
            # Troublehsooting print.
            # print ("WHOA")
        else:
            battleScreen.visible = False
        
            
def onMousePress (x,y):
    print (len(app.hitPoints))

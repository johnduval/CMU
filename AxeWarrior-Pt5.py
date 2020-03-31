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
# 
app.battleStarted = False

app.enemyHpMax = 8


# 
app.warriorAtk = 0
app.enemyAtk = 0
app.warriorDef = 0
app.enemyDef = 0

app.warriorAtkMAX = 8
app.enemyAtkMAX = 4
app.warriorDefMAX = 5
app.enemyDefMAX = 3

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
# Part 5 addition
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
enemeyDeadScreen = Group (
    Rect(0, 100, 400, 200, fill='blue', opacity=70),
    Label ("Enemey has 0 HIT POINTS.  YOU WIN  :)",200,200,size=20,fill='green')
    )
enemeyDeadScreen.visible = False

def enemyDead ():
    enemeyDeadScreen.visible = True
    enemeyDeadScreen.toFront()
    app.stop()
        
    
    
    
    
battleScreen = Group(
    Rect (0,0,400,400-app.movement,fill='grey', opacity = 75),
    Label ("FIGHT!", 200,50,size=50,fill='yellow',bold=True),
    Label("Warrior Stats", 100,100,size=25),
    Label("Enemy Stats", 300,100,size = 25),
    Label("Press 't' to Attack!",200,215,fill='blue',size=35)
    )
    
battleScreenData = Group ()
battleScreen.visible = False
battleScreenData.visible = False



# app.enemyHp = 0
# app.battleStarted = False
# app.warriorAtk = 0
# app.enemyAtk = 0
# app.warriorDef = 0
# app.enemyDef = 0


# Part 5
def battle (key):
    print ("----------")
    playerHp = len (app.hitPoints)
    if (app.battleStarted == False):
        app.enemyHp= randrange (2,app.enemyHpMax)
        app.warriorAtk = randrange (0,app.warriorAtkMAX)
        app.warriorDef = randrange(0,app.warriorDefMAX)
        app.enemyAtk = randrange(0,app.enemyAtkMAX)
        app.enemyDef = randrange(0,app.enemyDefMAX)
        app.battleStarted = True
    battleScreenData.clear()
    warriorHpLabel = Label(playerHp,130,125,size=20, fill = 'red')
    battleScreenData.add (warriorHpLabel)
    battleScreenData.add (Label("HP: ",100,125,size=20, fill = 'red'))
    battleScreenData.add (Label("Attack: " + str (app.warriorAtk),100,150,size=20,fill='red'))
    battleScreenData.add (Label("Defense: " + str (app.warriorDef),100,175,size=20,fill='red'))
    
    enemeyHpLabel = Label(app.enemyHp,330,125,size=20,fill = 'red')
    battleScreenData.add (enemeyHpLabel)
    battleScreenData.add (Label("HP: ",300,125,size=20, fill = 'red'))
    battleScreenData.add (Label("Attack: " + str (app.enemyAtk),300,150,size=20,fill='red'))
    battleScreenData.add (Label("Defense: " + str (app.enemyDef),300,175,size=20,fill='red'))
    print (app.warriorAtk)
    print (app.warriorDef)
    print (app.enemyAtk)
    print (app.enemyDef)
        
        # wa = randrange (0,app.warriorAtk)
        # wd = randrange(0,app.warriorDef)
        # ea = randrange(0,app.enemyAtk)
        # ed = randrange(0,app.enemyDef)
        # battleScreen.add (Label("Axe Warrior Stats", 100,100,size=25))
        # battleScreen.add (Label("HP: " + str(playerHp),100,125,size=20, fill = 'red'))
        # battleScreen.add (Label("Attack: " + str (wa),100,150,size=20,fill='red'))
        # battleScreen.add (Label("Defense: " + str (wd),100,175,size=20,fill='red'))
        # battleScreen.add (Label("Enemy Stats", 300,100,size = 25))
        # battleScreen.add (Label("HP: " + str(app.enemyHp),300,125,size=20, fill = 'red'))
        # battleScreen.add (Label("Attack: " + str (ea),300,150,size=20,fill='red'))
        # battleScreen.add (Label("Defense: " + str (ed),300,175,size=20,fill='red'))
        # battleScreen.add ()
        
    
    
    if (key == 't'):
        print ()
        battleScreen.add (Label("You attacked!",200,245,fill='purple',size=35))
        
        if (app.enemyAtk > app.warriorDef):
            warriorDelta = app.warriorDef - app.enemyAtk
            print ("warrior change in HP: " + str (warriorDelta))
            drawHearts(warriorDelta)
            playerHp = len (app.hitPoints)
            warriorHpLabel.value=playerHp
            # if (playerHp == 0):
        if (app.warriorAtk > app.enemyDef):
            enemyDelta = app.warriorAtk-app.enemyDef
            print (enemyDelta)
            app.enemyHp -= enemyDelta
            enemeyHpLabel.value = app.enemyHp
            if (app.enemyHp <= 0):
                enemyDead()
            
        
        
        
        
    # print (app.enemyHp)



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
            battleScreen.visible = True
# Part 5 added.
            battleScreenData.visible = True
            # part 5 = added parameter key
            battle(key)
            # Troublehsooting print.
            # print ("WHOA")
        else:
            battleScreen.visible = False
        
            
def onMousePress (x,y):
    print (len(app.hitPoints))

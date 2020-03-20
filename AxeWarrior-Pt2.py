#############################
###                       ###
### AXE WARRIOR - PART 1  ###
###                       ###
#############################

# Create global variables.
# Modify initializeGame (taken from tic-tac-toe)
# Create player's starting Hit Points (HP) in initializeGame()
# Create player movement (bounded motion)
# Obstacles
    # Unable to cross 6Mountains
    
    
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




app.rows = 9
app.cols = 10
app.board = makeList(app.rows, app.cols)
board = Group()
# Distance objects move in game (also same as each cell size)
app.movement = 0

fireSquares = Group ()
lifeSquares = Group ()
mountainSquares = Group ()
# Store player's hit points.
app.hitPoints = [ ]
app.heartUrl = 'https://pm1.narvii.com/6696/35ce165bcb7637f41c7597fc6761479655aa0c98_hq.jpg'
app.warriorUrl = 'https://a.wattpad.com/useravatar/Sunpool.256.143085.jpg'


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

# PART 2 - parameter hpChange will be the number of HPs you lose or gain
# it will be taken from the movement part of the code below.
def drawHearts (hpChange):
    # You'll be calculating current hp a number of times - use the following lein to do so.
    hp = len (app.hitPoints)
    print ("Starting HP: " + str (len(app.hitPoints)))
    # Check IF hpChange is below 0.  Think of this meaning your Warrior has lost health.
    if ...
        # Will go through the number of times you lose HP.
        for i in range (abs(hpChange)):
            # Calculate current hp
            hp = ...
            # Check if HP is less than or equal to 1 -  You've lost if so!
            # You know if you've lost HP and it's currently at 1, loosing any hp will bring you to 0.
            if ...
                ????? # Call your game over function.
            # Check if hp is greater than or equal to 1 so we can loose hp!
            if ...
                # Make the heart of the current index we're on not visible.
                app.hitPoints[hp-1].??? = ...
                # Remove the last element in our app.hitPoints.  What 2D list function do we use to remove elements?
                # (you do not need to specify the array element to remove as the function by default removes the last element)
                app.hitPoints.???
    # Now we're checking if we gained hp.  Yay!
    if ???
        # Use a For Loop to go through your hpChange.
        # Hint... What for loop did we use when we lost HP?
        for ...
            hp = ... # calculate current hp
            # This is how I added my heart... You may need to mess with values!!!
            # I also used .width and .height to modify my image - also can set its centerX & centerY that may make life easier. 
            app.hitPoints.append (Image (app.heartUrl, hp * app.movement + 8,357))
            app.hitPoints[hp].width /= 40
            app.hitPoints[hp].height /= 40
            app.hitPoints[hp].toBack()
        
        # Checks to see if lifeSquare should be removed after running over it.
        # Prevents infinite life.
        target = lifeSquares.hitTest(app.warrior.centerX, app.warrior.centerY)
        # Remove 'target' from lifeSquares group.
        ???
    # Print out your Ending HP - look at how we printed Starting HP!
    print ...
    # Print out how much your HP changes by... What function parameter tells us this??
    print ...


# Part 2
# Function to length of Groups by looped through its children.
# Used elsewhere in code.
def groupLength (g):
    # Set a counter equal to 0
    counter = 0
    for i in g.children:
        # Increase counter by 1
    # Return counter's value (make sure outside of For Loop!)
    

# PART 2: ADD RANDOMIZATION.
# In part 1, we simply drew squared.  Now we need to both randomize the number of squares
# AND make sure they're not drawn twice.
# NOTE: For part 2, your code in drawObstacles() may change drastically!
# Function draws area on map our player cannot pass, OR cause damage!
def drawObstacles ():
    
    #### Mountain Square Creation ####
    # (I SUGGEST GETTING MOUNTAIN SQUARES WORKING CORRECTLY BEFORE MOVING ON TO LIFE & FIRE SQUARES)
    # Create a local variable for the number of local mountain squares.
    # I choose RANDOM between 1 & 5 squares.
    number_ms ...
    # Print the number of mountain squares
    print ("Mountain #: " + str (number_ms))
    # Uses a while loop:
    # Check if the number of mountain squares we've drawn is equal to the group's length.
    # Notice how groupLength(mountainSquares) calls the groupLength function above and passes the corresponding Group.
    # This gets our number of Squares, and will draw them unti they are equally equal.
    while (number_ms != groupLength (mountainSquares)):
        # have 10 'x' tiles across, 9 'y' down.
        # Starts at 1 so we don't start on Warrior.
        x = randrange (1,10)
        y = ...
        # Check if our App.Board at [x][y] has anything drawn on the square we're trying to.
        # For instance, if x = 5 & y = 5, the IF will check if app.board[] has anything drawn at app.board[5][5]
        # If nothing is drawn, then add a square to mountainSquares & make that app.board square contain the proper boolean.
        if (app.board[y][x] == False):
            # Add your Rectangle to mountainSquares
            # Notice how I've changed how the Rectangle x & y coordinates change.  This allows them to be automatically calculated.
            mountainSquares.add (Rect (x*app.movement,y*app.movement,app.movement,app.movement,fill='grey'))
            # Set app.board at this location to the other boolean because there's now something on it. (look at the IF statement)
            app.board ...


    #### Fire Square Creation ####

    # NOW DO THE SAME THING FOR FIRE SQUARES AS WAS DONE IN MOUNTAIN
    

    
    #### Life Square Creation ####
    
    # NOW DO THE SAME THING FOR LIFE SQUARES.

    
drawObstacles()

# Defines gameOver and newGame screens.
newGameScreen = Group(
    Rect(0, 100, 400, 200, fill='aliceBlue', opacity=70),
    Label('Welcome to Axe Warrior!', 200, 190, fill='darkOrange', size=30,
          bold=True),
    Label('press space to start a new game', 200, 220, fill='darkOrange',
          size=15, bold=True)
    )
    
# PART 2
# We have a newGameScreen... Now we need a gameOverScreen!
# Draws and setss gameOverScreen.
gameOverScreen = Group ...  #do your game other thing.  Look at the newGameScreen Group or Tic-Tac-Toe for reference.
# Make gameOverScreen not visible!  Will become visible when loose.
gameOverScreen.visible = ...

# PART 2
# Create gameOver function
def ...
    # turn gameOverScreen visible. 
    gameOverScreen ...
    # Stop the app.
    ??? #Stop the app.
    
def onKeyPress(key):
    # Start a new game or restart the game.
    # When space is pressed and the game is not already playing,
    # make the newGameScreen invisible and set isGamePlaying.
    ### Place Your Code Here ###
    if (key == 'space'):
        if (app.isGamePlaying == False):
            app.isGamePlaying = True
            newGameScreen.visible = False
    
    # Moving right is down.
    # Fill out other movements!
    # Be sure to keep "bounded motion" in mind so the Warrior doesn't go off the Canvas!
    if (app.isGamePlaying == True):
        # print (app.hitPoints)
        # Storing player's current position.
        # This allows us to move player back to original position if goes out of bounds OR hits an object.
        warriorCurrentPos = [app.warrior.centerX, app.warrior.centerY]
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
        if (app.warrior.hitsShape (mountainSquares) == True):
            app.warrior.centerX = warriorCurrentPos[0]
            app.warrior.centerY = warriorCurrentPos[1]
        # PART 2
        # Test for hitting FIRE or LIFE squares
        # Check if app.warrior hits the fireSquares SHAPE.
        # Hint: Refer to 4.3.4 Shape Methods 2
        if ...
            # IF True, call the function that draws hearts.
            # Pass the number of life lost as your parameter.
            ???
        # Check if app.warrior hits the lifeSquares SHAPE.
        if ...
            # IF True, call the function that draws hearts.
            # Pass the number of life gained as your parameter.
            ???
            
# onMousePress can be used for debugging.  Not required.
def onMousePress (x,y):
    print (len(app.hitPoints))

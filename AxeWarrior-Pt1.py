#############################
###                       ###
### AXE WARRIOR - PART 1  ###
###                       ###
#############################
# BASIC REQUIREMENTS:
# Create global variables.
# Modify initializeGame (taken from tic-tac-toe)
# Create player's starting Hit Points (HP) in initializeGame()
# Create player movement (bounded motion)
# Obstacles
    # Unable to cross Mountains

# In following 3 lines: Create a 2D list with 9 rows and 10 columns.  Assign the values to app.rows & app.cols, and use those to create your board.
app.rows = ...
app.cols = ...
app.board = ... #Create your empty 2D list here.
board = ... #Create an empty Group

# Distance objects move in game (also same as each cell size that will be calculated below)
app.movement = 0

# Create empty Groups for the following 3 "squares"...
fireSquares = ... 
lifeSquares = ...
mountainSquares = ...
# Stores player's hit points - initially create it as an empty list.
app.hitPoints = ...
# Image that will be your player's hit point designation.  Keep in mind, this will be resized to ~ 20 x 20 pixels
app.heartUrl = ...
# Image for your Warrior.  Will be resized to 38 x 38 pixels later in program.
app.warriorUrl = ...


def initializeGame():
    # Create the board and initialize game properties.
    cellSize = 400 / 10
    # Lets us know how far objects should move in 1 turn. -  should be the lebgth of 1 cell!
    app.movement = cellSize
    # Creates our board...
    for row in range(app.rows):
        for col in range(app.cols):
            x = col * cellSize
            y = row * cellSize
            board.add(
                Rect(x, y, cellSize, cellSize, fill='???,
                     border=???, borderWidth=1)
                )
    
    # Create your warrior by making it an Image with app.warriorUrl.  Start at coordinate 1,1 with a widht of 38,38.
    # (We want to make sure the image does not overlap more than 2 squares!!)
    app.warrior = ...

    
    # Player's starting HP - how much life should your character start with?
    HPs = ...
    # Draw player hearts.
    for i in range (HPs):
        # This will be the 'x' location of your image.
        # You'll want to multiply your for loops's looping variable * size of the cell.  And then add a number so the hearts don't start at 0.
        # Adjust values untill each HP image is visible!
        x = ... 
        # append Image to "app.hitPoints".  You'll need to use your heart's URL, 'x' form above, and you'll need to adjust the 'y' accordingly.
        # Modify both app.hitPoint's width and height so they fit in the white space.
        # app.hitPoints index should be the loop's looping variable.
        app.hitPoints[?].??? = ...   # width
        app.hitPoints[?].??? = ...   # height
        # send app.hitPoint[i] to the back.
        app.hitPoints[?].???
        
    # The game status
    app.isGamePlaying = False

initializeGame()

#Draws area on map our player cannot pass, OR cause damage!
def drawObstacles ():
    # create 2 "mountain" squares and assign them to their own local variable.  They can either be a Rect or an Image.
    # In either case, they need to exactly 40x40 pixels and start precisely on 1 tile:
    ms1 = Rect (40,120,app.movement,fill,app.movement,fill,fill=???)
    ms2 = ???
    # Add the 2 mountain squares you just created to mountainSquares Group.
    mountainSquares.add ???????
    # Do the same for Fire & Life squres.  Create 2 of each type, and then add them to their respective Groups.
    # They currently will not do anything, but will when we add in loosing and gaining HP.
    
drawObstacles()

# Defines gameOver and newGame screens.
newGameScreen = Group(
    Rect(0, 100, 400, 200, fill=???, opacity=70),
    Label('Welcome to Axe Warrior!', 200, 190, fill=???, size=30,
          bold=True),
    Label('press space to start a new game', 200, 220, fill='???,
          size=15, bold=True)
    )
    

def onKeyPress(key):
    # Start a new game or restart the game.
    # When space is pressed and the game is not already playing,
    # make the newGameScreen invisible and set isGamePlaying.
    ### Place Your Code Here ###
    if (key == 'space'):
        if (app.isGamePlaying == False):
            # Set game playing boolean to True!
            # Make the new screen label & rectangle Group no longer visible.
    
    # Moving right is down.
    # Fill out other movements!
    # Be sure to keep "bounded motion" in mind so the Warrior doesn't go off the Canvas!
    if (app.isGamePlaying == True):
        # Storing player's current position.
        # This allows us to move player back to original position if goes out of bounds OR hits an object.
        warriorCurrentPos = [app.warrior.centerX, app.warrior.centerY]
        if (key == 'right'):
            app.warrior.centerX += app.movement
        # Fill out out movements for other keys.
        
        # Check IF app.warrior is outside the canvas bounds.
        # IF so, set warrior's back to values from warriorCurrentPos.
        if (... warrior outside of Canvas Bounds ...):
            app.warrior.centerX = warriorCurrentPos[?????]
            # Set warrior's Y
        # use hitsShape to see if warrior hits mountainSquares.
        # IF True, set warrior's back to values from warriorCurrentPos.
        if (????):
            # Reset warrior back to current position.

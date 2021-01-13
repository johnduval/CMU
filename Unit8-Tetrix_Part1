# Set steps per second to 10
app.stepsPerSecond = 5



# Global variables you'll need
app.blockWidth = 19
# Use when moving the shape's centerX or centerY to keep it aligned in the grid.
app.blockMove = 20
app.shapeName = ''

# Group to add your grid Rectangles to.
grid = Group ()


# Create the Tetrix grid using a Nested For Loop.  Each block (Rect) should be 20 pixesl H x 20 pixel W.
# Create the grid effect by using a border with your Rects.
# Be sure to add your Rect to the grid Group.

# Nested For loop 1
    # Nested For Loop 2
        # Add / Create your Rect.

# Label to display the speed in the upper right block.  It's value should be the app.stepsPerSecond
speed = 

# Group that will contain the current "Tetris" Piece
shape = Group()
# Group to contain all pieces when they've stopped moving.
allShapes = Group ()


# Def to create the tetromino shape!
def tetromino ():
    # This is the first Rect in the tetromino (the long 4-square piece).  Create the other 3 pieces.
    # Making the pieces being perfectly aligned inside the Rect's is crucial!!!
    shape.add (Rect (141, 1, app.blockWidth,app.blockWidth, fill = gradient('yellow','orange')))
    
    app.shapeName = 'tetromino'


# Def to create the tetracube!
def tetracube ():
    # This is the first Rect in the tetracube (square).  Create the other 3 pieces.
    # Making the pieces being perfectly aligned inside the Rect's is crucial!!!
    
    shape.add (Rect (141,1,app.blockWidth,app.blockWidth, fill = gradient('yellow','orange'))

    app.shapeName = 'tetracube'


# Function to 1) Add the current shape to the allShapes.  and 2) create a new shape.
def nextShape ():
    
    # Add current Tetris piece to the allShapes.
    for currentShape in shape:
        allShapes.add (Rect (currentShape.left, currentShape.top, currentShape.width, currentShape.height, fill = gradient('green','grey')))


    # Remove the current tetris piece
    shape. ???
    
    # Create a local helper variable, with a possible random value of 0 or 1
    randShape = ???
    # if value is 0, call the tetracube function.  If the value is 1, call randShape function. 
    
    if ....???


# Keep here!  Draws shape when we press play.
nextShape()



def onKeyPress (key):
    # if we press 'right', move the tetris piece one "square" to the right.  Make sure it keeps aligned inside the grid
    # Do the same for 'left'
    # Keep the entire tetris piece bound inside the canvas.  Pieces may not go outside the grid!!
    if... ???

    
    # Be able to change the app speed between 0 (pause) and 9 (fastest).  Update both app.StepsPerSecond AND the label displaying the speed.

    if ... ???
        
        
        

def onStep ():
    # Move the current Tetris shape down the Canvas.  Again - make sure it stays aligned inside the group.
    shape.centerY += app.blockMove
    # If bottom of the shape is equal to 400, call nextShape.
    # This should be what causes the blocks to stay in place when they reach the bottom, and create your new Tetris shape.
    if ....?
        Call the correct function here!

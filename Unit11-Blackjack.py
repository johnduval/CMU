# Create your values list!
app.values = ...
# Create your Suits list!
app.suits = ...
# this will be your List containing your hands.
app.player1hand = []

#Label wiith instructions.
app.intructions = ...
#3 different Labels for:
# 1) PLAYER 1
# 2) YOU DREW
# 3) YOUR CURRENT HAND

# Rectangle background for where your cards are displayed.
p1display = Rect (10,110,150,75,fill='yellow',opacity=50,border='black')
# Current value of card you just drew
app.cardValue =  Label ("No Card!", 50,100)
# Current suit of card you just drew
app.cardSuit = Label ("No Card!", 100,100)
# Numerical valye of all cards you've drawn
app.p1handValue = Label (0, 75,150, size = 20)
# All cards in P1 hand.
app.currentp1hand = Group (Label ("No cards!", 75,175))

def onKeyPress (key):
	#IF 'd' is pressed, call 4 functions in the code (in order of they're listed):
        
        
        
        
    # IF 's' is pressed, stop App until next step...
        

#Draws a new card for Player 1.
def drawCard_p1():
	#new newVal & newSuit: Value should be a RANDOM value of the "app.values" list & "app.suits" list.  Hint: You'll be starting at index 0, and going to the LENgth of the List.
	newVal = ...
    newSuit = ...
    # Set app.cardValue equal to the newVal index you got from above.  For example: If newSuit returns [2], then app.cardSuit.value would be equal to 'Diamonds'
    app.cardValue.value = ...
    app.cardSuit.value = ...
	# Following line adds both the value & suit the app.player1hand
    app.player1hand.append([app.values [newVal],app.suits [newSuit]])

#Displays all of P1's cards.
def drawHand ():
    # print (app.player1hand)   #Line is usefor for debugging what is going on!
    # Clear app.currentp1hand. (basically resetting the display of current hand display
	
    # Create a for loop, using the length of app.player1hand as our range.
	for ...
        # ADD Label (app.player1hand[i],75,175 + (i * 25) to app.currentp1hand.
		# Try messing around with the values to see what happens.
		
		#Update p1display's height.  Multiply 25 * length of app.player1and, and add 50.  Again, mess aroung with values.
        p1display.height=(len(app.player1hand) * 25) + 50

# Caulcate's Player 1's hand score.
def calcP1hand():
    # Add the value of the card to app.p1handValue.  If it's 2-10, just add the number (hint: these are the only digits, so check for that).
	# If it's J-K, add 10.
	# If it's an Ace, add 11.

# Disaplts game over.
def gameOver():
	# is the score > 21?  Displat GAME OVER and app.stop() if so.    

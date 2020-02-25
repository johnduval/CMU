# Create your values list!
app.values = ...
# Create your Suits list!
app.suits = ...
# this will be your List containing your hands.
app.player1hand = ...
# Dealer's hand
app.dealer1hand = ...

# Change instruction for DEALER to start!
app.intructions = ...
# 3 different Labels for:
# 1) PLAYER 1
# 2) YOU DREW
# 3) YOUR CURRENT HAND
# AND.... Another 3 different labels for...
# 1) Dealer
# 2) Dealer Drew
# 3) Dealer Current Hand
# Rectangle background for where your cards are displayed.
p1display = Rect (10,110,150,75,fill='yellow',opacity=50,border='black')
app.p1cardValue =  Label ("No Card!", 50,100)
app.p1cardSuit = Label ("No Card!", 100,100)
app.p1handValue = Label (0, 75,150, size = 20)
app.currentp1hand = Group (Label ("No cards!", 75,175))

#Now do the same thing, only replacing all content from p1 (player 1) with that for d1 (dealer 1):
d1display = Rect (210,110,150,75,fill='yellow',opacity=50,border='black')
app.d1cardValue =  ...
app.d1cardSuit = ...
app.d1handValue = ...
app.currentd1hand = ...

# Tells us if dealer has started
app.d1started = False
# Has Player 1 stood?
app.p1stand = False
# Has player 1 started their game yet, to draw 2 cards?
app.p1Started = False

# Draws Dealer's first card to get the game started!
def onMousePress (mouseX, mouseY):
	#Check IF app.p1Started is false.
    #
	    # Change app.d1started to true.
		# Call drawCard_dealer(), drawHand_d1(), & calcD1hand()
		# change app.intructions's value to tell Player how how to draw a card or stand.
      
def onKeyPress (key):
    # Compound IF statement asking if app.d1started is True and if app.p1stand is False - basically run this block if player 1 has started, but has not stood.
		# Check if 'd' is pressed...		
            # IF app.app.p1Started is False (meaning player one has not started):
                # Call the 3 functions that draw p1's card, draw p1's hand, and calculate P1's hand
                # Set app.p1Started to True
            #Call the 4 functions from IF 'd's is pressed in the Blackjack_pt1.
        if (key == 's'):
            # Rect (0,300,400,100,fill='red')
            # Label ("Time for the dealer...to be continued", 200,350,size=20)
            app.p1stand = True
            # app.stop()
            app.intructions.value = "Press 'space' for dealer to go!"
    # Check if app.p1stand is True.
		# Get key input for Dealer to draw their card.  Ie, check if input key is 'space'.
            # Call 4 functions: 1) Draw card for dealer, draw hand for dealer, Calculation dealer hand, and game over.
        

def drawCard_p1():
    #new newVal & newSuit: Value should be a RANDOM value of the "app.values" list & "app.suits" list.  Hint: You'll be starting at index 0, and going to the LENgth of the List.
	newVal = ...
    newSuit = ...
    # Set app.cardValue equal to the newVal index you got from above.  For example: If newSuit returns [2], then app.cardSuit.value would be equal to 'Diamonds'
    app.cardValue.value = ...
    app.cardSuit.value = ...
	# Following line adds both the value & suit the app.player1hand
    app.player1hand.append([app.values [newVal],app.suits [newSuit]])
    
def drawCard_dealer():
    #new newVal & newSuit: Value should be a RANDOM value of the "app.values" list & "app.suits" list.  Hint: You'll be starting at index 0, and going to the LENgth of the List.
    newVal = ...
    newSuit = ...
    # Set values equal to the INDEX of ones you got from above - just like in def drawCard_p1():
    app.d1cardValue.value = ...
    app.d1cardSuit.value = ...
    app.dealer1hand.append([app.values [newVal],app.suits [newSuit]])

def drawHand_p1 ():
    # print (app.player1hand)   #Line is usefor for debugging what is going on!
    # Clear app.currentp1hand. (basically resetting the display of current hand display
	
    # Create a for loop, using the length of app.player1hand as our range.
	for ...
        # ADD Label (app.player1hand[i],75,175 + (i * 25) to app.currentp1hand.
		# Try messing around with the values to see what happens.
		
		#Update p1display's height.  Multiply 25 * length of app.player1and, and add 50.  Again, mess aroung with values.
        p1display.height=(len(app.player1hand) * 25) + 50
        
def drawHand_d1 ():
	# Clear app.currentd1hand
    app.currentd1hand.clear()
	# Create a for loop, using the length of app.dealer1hand as our range.
        # ADD Label (app.dealer1hand[i],275,175 + (i * 25) to app.currentd1hand
		#Update d1display's height.  Refer to def drawHand_p1 (): on an idea on how to do so!
        d1display.height= ...

#Calculate total of Player 1's hand.
def calcP1hand():
    # Use app.p1cardValue.value to Add the value of the card to app.p1handValue.  If it's 2-10, just add the number (hint: these are the only digits, so check for that).
	# If it's J-K, add 10.
	# If it's an Ace, add 11.
        
# Calculate total of Dealer's hand.
def calcD1hand():
	# Use app.d1cardValue.value to Add the value of the card to d1handValue.value.  If it's 2-10, just add the number (hint: these are the only digits, so check for that).
	# If it's J-K, add 10.
	# If it's an Ace, add 11.

def gameOver():
	# IF the score of player 1's hand value > 21?  Display GAME OVER and app.stop() if so. 
    
    
	# CHeck if P1 has stood (hint: Boolean):
		# use the rules to display who has won!
		
		# Has dealer busted?
		# IF Not...
        	# Does Dealer beat Player?
			# Does Player beat Dealer?
			# Is it a tie??
            

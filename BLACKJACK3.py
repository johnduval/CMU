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

#changing for pt3
# Change instruction for PLAYER TO BET!!!
app.intructions = ...
# 3 different Labels for:
# 1) PLAYER 1
# 2) YOU DREW
# 3) YOUR CURRENT HAND
# AND.... Another 3 different labels for...
# 1) Dealer
# 2) Dealer Drew
# 3) Dealer Current Hand

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


# NEWs

#Create an empty group called "roundMessage"

#Set the following two booleans to False.
app.p1betPlaced = ...
app.roundOver = ...

Label ("Player 1 current has $ ", 75,27,fill='purple')
app.p1money = Label(100,170,27,fill='green',bold=True)
Label ("Player 1 has bet $ ", 250,27,fill='purple')
app.p1bet = Label (0,340,27,fill='green',bold = True)
Rect (10,38,380,20,border = 'black',fill='grey',opacity=20)

####
def onMousePress (mouseX, mouseY):
    # new
    if (app.p1betPlaced == False):
        response = app.getTextInput('Place your bet between 1 and ' + str(app.p1money.value))
        if (response.isdigit() == True and int(response) > 0 and int(response) <= app.p1money.value):
            app.p1bet.value = int(response)
            app.p1betPlaced = True
    
    # Check IF app.p1Started is false AND if app.p1betPlaced is True
    	# Change app.d1started to true.
		# Call drawCard_dealer(), drawHand_d1(), & calcD1hand()
		# change app.intructions's value to tell Player how how to draw a card or stand.
        

def onKeyPress (key):
    # Compound IF statement asking if app.d1started is True and if app.p1stand is False and if app.roundOver is False - basically run this block if player 1 has started, but has not stood.
		# Check if 'd' is pressed...
            # IF app.app.p1Started is False (meaning player one has not started):
                # Call the 3 functions that draw p1's card, draw p1's hand, and calculate P1's hand
                # Set app.p1Started to True
	        #Call the 4 functions from IF 'd's is pressed in the Blackjack_pt1.
        if (key == 's'):
            app.p1stand = True
            app.intructions.value = "Press 'space' for dealer to go!"
	# Check if app.p1stand is True.  Now also check if app.roundOver is False!
		# Get key input for Dealer to draw their card.  Ie, check if input key is 'space'.
            # Call 4 functions: 1) Draw card for dealer, draw hand for dealer, Calculation dealer hand, and game over.
    # Check if both app.roundOver is True & and key 'enter' has been pressed.
		# Call roundReset function if so

# new function to reset for a new round.
def roundReset ():
    # Clear group app.currentp1hand
    # Clear group app.currentd1hand
	# Reset app.p1handValue & app.d1handValue.value back to 0
    # Reset app.player1hand & app.dealer1hand back to being empty Lists.
	# Reset app.intructions's value instructing to Press anywhere on Canvas for player 1 to bet.
 	# Reset app.p1cardValue.value, app.p1cardSuit.value, app.d1cardValue.value, & app.d1cardSuit.value back to "No Card"
    # Reset p1display & d1display's height back to 75
	# Clear roundMessage
	# Set to False: app.d1started, app.p1stand, app.p1Started, app.p1betPlaced, app.roundOver

# Or use code from Blackjack_pt2
def drawCard_p1():
    #new newVal & newSuit: Value should be a RANDOM value of the "app.values" list & "app.suits" list.  Hint: You'll be starting at index 0, and going to the LENgth of the List.
	newVal = ...
    newSuit = ...
    # Set app.cardValue equal to the newVal index you got from above.  For example: If newSuit returns [2], then app.cardSuit.value would be equal to 'Diamonds'
    app.cardValue.value = ...
    app.cardSuit.value = ...
	# Following line adds both the value & suit the app.player1hand
    app.player1hand.append([app.values [newVal],app.suits [newSuit]])
    
	# Or use code from Blackjack_pt2
def drawCard_dealer():
    #new newVal & newSuit: Value should be a RANDOM value of the "app.values" list & "app.suits" list.  Hint: You'll be starting at index 0, and going to the LENgth of the List.
    newVal = ...
    newSuit = ...
    # Set values equal to the INDEX of ones you got from above - just like in def drawCard_p1():
    app.d1cardValue.value = ...
    app.d1cardSuit.value = ...
    app.dealer1hand.append([app.values [newVal],app.suits [newSuit]])

	# Or use code from Blackjack_pt2
def drawHand_p1 ():
    # print (app.player1hand)   #Line is usefor for debugging what is going on!
    # Clear app.currentp1hand. (basically resetting the display of current hand display
	
    # Create a for loop, using the length of app.player1hand as our range.
	for ...
        # ADD Label (app.player1hand[i],75,175 + (i * 25) to app.currentp1hand.
		# Try messing around with the values to see what happens.
		
		#Update p1display's height.  Multiply 25 * length of app.player1and, and add 50.  Again, mess aroung with values.
        p1display.height=(len(app.player1hand) * 25) + 50

# Or use code from Blackjack_pt2
def drawHand_d1 ():
    # Clear app.currentd1hand
    app.currentd1hand.clear()
	# Create a for loop, using the length of app.dealer1hand as our range.
        # ADD Label (app.dealer1hand[i],275,175 + (i * 25) to app.currentd1hand
		#Update d1display's height.  Refer to def drawHand_p1 (): on an idea on how to do so!
        d1display.height= ...

# Or use code from Blackjack_pt2
def calcP1hand():
    # Use app.p1cardValue.value to Add the value of the card to app.p1handValue.  If it's 2-10, just add the number (hint: these are the only digits, so check for that).
	# If it's J-K, add 10.
	# If it's an Ace, add 11.

# Calculate total of Dealer's hand.	
def calcD1hand():
    # Use app.d1cardValue.value to Add the value of the card to d1handValue.value.  If it's 2-10, just add the number (hint: these are the only digits, so check for that).
	# If it's J-K, add 10.
	# If it's an Ace, add 11.


# ****** change your game over shapes (rectangles & Labels) to be part of "roundMessage" Group.  They will get removed in def roundReset ()
def gameOver():
    if (app.p1handValue.value > 21):
        app.p1money.value -= app.p1bet.value
        roundMessage.add (Rect (0,300,400,100,fill='red'))
        roundMessage.add (Label ("YOU DREW "+ str (app.p1handValue.value)+". YOU LOSE!", 200,325,size=25))
        roundMessage.add (Label ("Press 'enter' to start a new round!", 200,375,size = 25))
        # roundMessage.add( Circle(200, 200, 20, fill='cyan', border='black'))
        app.roundOver = True
        app.roundOver = True
    
    if (app.p1stand == True):
        if (app.d1handValue.value > 21):
            app.p1money.value += app.p1bet.value
            roundMessage.add (Rect (0,300,400,100,fill='red'))
            roundMessage.add (Label ("DEALER DREW "+ str (app.d1handValue.value)+". DEALER BUSTS.  YOU WIN!", 200,325,size=17))
            roundMessage.add (Label ("Press 'enter' to start a new round!", 200,375,size = 25))
            app.roundOver = True
            app.roundOver = True
            print ("!!!!!")
            
        elif (app.d1handValue.value >= 17):
            if (app.d1handValue.value > app.p1handValue.value):
                app.p1money.value -= app.p1bet.value
                roundMessage.add (Rect (0,300,400,100,fill='red'))
                roundMessage.add (Label ("Dealer Drew "+ str (app.d1handValue.value)+" to player's " + str(app.p1handValue.value) + ". Dealer wins!", 200,325,size=10))
                roundMessage.add (Label ("Press 'enter' to start a new round!", 200,375,size = 25))    
                app.roundOver = True
                app.roundOver = True
                print ("dealer wins")
            elif (app.d1handValue.value == app.p1handValue.value):
                app.p1money.value -= 0
                roundMessage.add (Rect (0,300,400,100,fill='red'))
                roundMessage.add (Label ("Dealer Drew "+ str (app.d1handValue.value)+" to player's " + str(app.p1handValue.value) + ". It's a tie!", 200,325,size=10))
                roundMessage.add (Label ("Press 'enter' to start a new round!", 200,375,size = 25))
                app.roundOver = True
                app.roundOver = True
                print ("TIE")
            else:
                roundMessage.add (Rect (0,300,400,100,fill='red'))
                app.p1money.value += app.p1bet.value
                roundMessage.add (Label ("Dealer Drew "+ str (app.d1handValue.value)+" to player's " + str(app.p1handValue.value) + ". Player 1 wins!", 200,325,size=10))
                roundMessage.add (Label ("Press 'enter' to start a new round!", 200,375,size = 25))
                app.roundOver = True
                app.roundOver = True
                print ("player 1 wins")
            

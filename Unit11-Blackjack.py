# Create your values list!
app.values = 
# Create your Suits list!
app.suits = 
# this will be your List containing your hands.
app.player1hand = []

#Label wiith instructions.
app.intructions 
#Labels for:
# PLAYER 1
# YOU DREW
# YOUR CURRENT HAND

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
        drawCard_p1()
        drawHand()
        calcP1hand()
        gameOver()
    IF 's' is pressed, stop App until next step...
        

def drawCard_p1():
	#new newVal & newSuit: Value should be a RANDOM value of the "app.values" list & "app.suits" list.  Hint: You'll be starting at index 0, and going to the LENgth of the List.
	newVal = ...
    newSuit = ...
    # Set app.cardValue equal to the newVal index you got from above.  For example: If newSuit returns [2], then app.cardSuit.value would be equal to 'Diamonds'
	app.cardValue.value = ...
    app.cardSuit.value = ...
	
    app.player1hand.append([app.values [newVal],app.suits [newSuit]])

def drawHand ():
    # print (app.player1hand)
    app.currentp1hand.clear()
    for i in range (len(app.player1hand)):
        app.currentp1hand.add(Label (app.player1hand[i],75,175 + (i * 25)))
        p1display.height=(len(app.player1hand) * 25) + 50

def calcP1hand():
    if (app.cardValue.value.isdigit() == True):
        # print ("digit!")
        app.p1handValue.value += int(app.cardValue.value)
    elif (app.cardValue.value != 'Ace'):
        app.p1handValue.value += 10
    else:
        app.p1handValue.value += 11
        # one = Label ('Ace = 1', 50,300)
        # elevel = Label ('Ace = 11', 200,300)
        # while (one.hits)

def gameOver():
    if (app.p1handValue.value > 21):
        Rect (0,300,400,100,fill='red')
        Label ("YOU DREW "+ str (app.p1handValue.value)+". YOU LOSE!", 200,350,size=25)
        app.stop()
    

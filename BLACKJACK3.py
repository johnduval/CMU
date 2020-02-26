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
        
    if (app.d1started == False and app.p1betPlaced == True):
        app.d1started = True
        drawCard_dealer()
        drawHand_d1()
        calcD1hand()
        app.intructions.value = "Press 'd' to draw a card, or 's' to Stand!"
        

def onKeyPress (key):
    # added app.rounderOver conditional.
    if (app.d1started == True and app.p1stand == False and app.roundOver == False):
        if (key == 'd'):
            if (app.p1Started == False):
                drawCard_p1()
                drawHand_p1()
                calcP1hand()
                app.p1Started = True
            drawCard_p1()
            drawHand_p1()
            calcP1hand()
            gameOver()
        if (key == 's'):
            # Rect (0,300,400,100,fill='red')
            # Label ("Time for the dealer...to be continued", 200,350,size=20)
            app.p1stand = True
            # app.stop()
            app.intructions.value = "Press 'space' for dealer to go!"
    
    # added app.rounderOver conditional.
    if (app.p1stand == True and app.roundOver == False):
        if (key == 'space'):
            drawCard_dealer()
            drawHand_d1()
            calcD1hand()
            gameOver()
        # app.intructions.value = "Press 'space' for dealer to go!"
    # new for starting new round.
    if (app.roundOver == True and key == 'enter'):
        roundReset ()

# new function to reset for a new round.
def roundReset ():
    print ('new game')
    app.currentp1hand.clear()
    app.currentd1hand.clear()
    app.p1handValue.value = 0
    app.d1handValue.value = 0
    app.player1hand = []
    app.dealer1hand = []
    app.intructions.value = "Press anywhere where on the Canvas for Player 1 to bet!"
    app.p1cardValue.value = "No Card!"
    app.p1cardSuit.value = "No Card!"
    app.d1cardValue.value = "No Card!"
    app.d1cardSuit.value = "No Card!"
    p1display.height = 75
    d1display.height = 75
    roundMessage.clear()
    app.d1started = False
    app.p1stand = False
    app.p1Started = False
    app.p1betPlaced = False
    app.roundOver = False

def drawCard_p1():
    newVal = (randrange (0,len(app.values)))
    newSuit = (randrange (0,len(app.suits)))
    app.p1cardValue.value = app.values [newVal]
    app.p1cardSuit.value = app.suits [newSuit]
    app.player1hand.append([app.values [newVal],app.suits [newSuit]])
    
def drawCard_dealer():
    newVal = (randrange (0,len(app.values)))
    newSuit = (randrange (0,len(app.suits)))
    app.d1cardValue.value = app.values [newVal]
    app.d1cardSuit.value = app.suits [newSuit]
    app.dealer1hand.append([app.values [newVal],app.suits [newSuit]])

def drawHand_p1 ():
    # print (app.player1hand)
    app.currentp1hand.clear()
    for i in range (len(app.player1hand)):
        app.currentp1hand.add(Label (app.player1hand[i],75,175 + (i * 25)))
        p1display.height=(len(app.player1hand) * 25) + 50
        
def drawHand_d1 ():
    app.currentd1hand.clear()
    for i in range (len(app.dealer1hand)):
        app.currentd1hand.add(Label (app.dealer1hand[i],275,175 + (i * 25)))
        d1display.height=(len(app.dealer1hand) * 25) + 50

def calcP1hand():
    if (app.p1cardValue.value.isdigit() == True):
        # print ("digit!")
        app.p1handValue.value += int(app.p1cardValue.value)
    elif (app.p1cardValue.value != 'Ace'):
        app.p1handValue.value += 10
    else:
        app.p1handValue.value += 11
        # one = Label ('Ace = 1', 50,300)
        # elevel = Label ('Ace = 11', 200,300)
        # while (one.hits)
        
def calcD1hand():
    if (app.d1cardValue.value.isdigit() == True):
        # print ("digit!")
        app.d1handValue.value += int(app.d1cardValue.value)
    elif (app.d1cardValue.value != 'Ace'):
        app.d1handValue.value += 10
    else:
        app.d1handValue.value += 11
        # one = Label ('Ace = 1', 50,300)
        # elevel = Label ('Ace = 11', 200,300)
        # while (one.hits)


# change your game over shapes (rectangles & Labels) to be part of "roundMessage" Group.
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
            

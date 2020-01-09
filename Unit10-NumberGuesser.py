# used to get user input with app.getTextInput. 
app.numberInput = ''
# initialize variables to use inside our functions.
app.number = 0
app.guess = 0
# Say hello to the Label.
Label ("Welcome to NUMBER GUESSER!", 200,25,size = 15, fill = 'blue')
# Tells user what to do!
intructions = Label ("Press 'Space' for Player 1 to start!", 200,65,size = 14, fill = 'purple')
# displays how player 2 is doing (guesses too high, low, or correct)
status = Label ("", 200,180,size = 15, fill='green')
# When getting use input, is used to see if P1 has has entered a number yet.  If yes, then turns True so can go to P2.
app.gameStarted = False
# displays P2 guesses
guess = Label ("", 200,150,size=20)
Label ("Number of guesses: ", 150,250,size=30)
# Updates every time a successful guess is made.
numberGuesses = Label (0,350,250,size = 30)
# background to make guesses look rad.
Rect (350,250,50,30,align = 'center', opacity=30,fill='purple',border='black')

# All P2 guesses get added to this group.
guesses = Group ()
# Background rects for all the P2 guesses - indicated if high / low / correct.
rects = Group ()
# Oh look, another Label!
player2guesses = Label("Player 2 Guesses (black dot indicates best guess. Red boxes is top low; yellow boxes too high):", 200,300,size=9,visible=False)
# Initialize variable to keep track of P2 best guess.  After First Guess, update variable if needed.
app.bestGuess = 0
# Difference betwwen P2's guess and app.bestGuess (absolute zero so always positive)
app.difference = 0
# When checking for the best guess, we use an IF to see if this is True to set the P2 guess to app.bestGuess since there's no other guess to check.  Set to False after first guess.
app.firstGuess = True
# Compare P2's guess to app.bestGuess.  Move the indicator if needed.  Update app.bestGuess if this moves.
app.bestGuessIndicater = Circle (40,350,5,visible = False)

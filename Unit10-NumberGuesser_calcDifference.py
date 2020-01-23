def calcDifference():
    for x in guesses.children:
        print ('in the guesses FOR loop')
        app.difference = abs (app.number - int(x.value))
        print ("difference: " + str(app.difference))
        if (app.firstGuess == True):
            app.bestGuessIndicater.visible = True
            app.firstGuess = False
            app.bestGuess = app.difference
        else:
            if (app.difference < app.bestGuess):
                app.bestGuessIndicater.centerX=10 + numberGuesses.value * 30
                app.bestGuess = app.difference
                print ("MOVE ")
        # app.bestGuess = difference
        print ("app.bestGuess: "+ str (app.bestGuess))

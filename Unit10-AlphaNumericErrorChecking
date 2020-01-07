app.message = ''
Label ("Press Space to enter a NUMBER", 200,50,size = 15, fill = 'blue')
Label ("Current User Input:", 200,150,size=20)
userInput = Label ("[currently no user input]", 200,200,size = 22, fill='red')

def onKeyPress (key):
	if (key == 'space'):
        app.message = app.getTextInput ("input a number")
    if (app.message.isdigit() == True):
        userInput.value = app.message
    else:
        userInput.value = "ERROR.  PLEASE ENTER A NUMBER!"

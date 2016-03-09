import getpass

# getPassword()
#	Asks the user for a password
#	Returns: The password
def getPassword():
	return getpass.getpass()

# getNonEmptyInput()
#	Prompt the user for an input which can't be empty, and repeat asking for
#	it until a valid input is given
def getNonEmptyInput(prompt):
	while True:
		result = input(prompt)
		if result != "":
			return result
		print("Error: This input may not be empty.")

# getIntegerInput()
#	Prompt the user for an input which must be an integer
#	Returns: the integer entered
def getIntegerInput(prompt):
	while True:
		result = input(prompt)
		try:
			return int(result)
		except ValueError:
			print("Error: Value entered was not a number")

# getValidatedInput()
#	Prompt the user for an input with a custom function to check for
#	a valid input.
def getValidatedInput(prompt, validFunc):
	while True:
		result = input(prompt)
		isValid = validFunc(result)
		if isValid == True:
			return result
		else:
			print("Error: " + isValid)

# getYesNoInput()
#	Prompt the user for a yes/no input. 
#	Returns: True for yes, False for no.
def getYesNoInput(prompt):
	while True:
		result = input(prompt).lower()
		if result in ['y', 'yes']:
			return True
		elif result in ['n', 'no']:
			return False
		else:
			print("Error: `y' or `n' expected.")

# getUsernameAndPassword()
#	Asks the user for a username and password
#	Returns: username, password
def getUsernameAndPassword():
	# Ask for a username until the user provides one
	user = getNonEmptyInput("Username: ")

	# Get the password
	password = getPassword()

	# Return them
	return user, password


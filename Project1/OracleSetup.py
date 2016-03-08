import sys
import cx_Oracle
import userInput

# getConnString(username, password)
#	Gets the connection string to oracle given a username and password
def getConnString(username, password):
	return '' + username + '/' + password + '@gwynne.cs.ualberta.ca:1521/CRS'

# connectOracle()
#   Asks the user for a username and password, and tries to connect to oracle
#   using them, returning the connection if successful. If unsuccessfull,
#   requests alternative passwords until successfull.
def connectOracle():
	user, password = userInput.getUsernameAndPassword()
	while True:
		connString = getConnString(user, password)
		try:
			connection = cx_Oracle.connect(connString)
			print("Login Sucessful!\n")
			return connection
		except:
			print("Incorrect, please enter the correct password.")
			password = userInput.getPassword()

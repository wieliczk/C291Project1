# Requires oracle login string
# Gets owners SIN and Vehicle ID

import cx_Oracle
import sys
import userInput

def isValidVehicleType(conn, type_id):
	# TODO: use database
	return False

def setupVehicleRegImpl(conn):
	print("\nNew Vehicle Registration\n")

	# TODO make sure serial_no not in database, return invalid serial no
	serial_no = userInput.getNonEmptyInput("Enter Vehicle serial #: ")

	# Basic fields with no validation needed
	maker = userInput.getNonEmptyInput("Enter Vehicle maker name: ")
	model = userInput.getNonEmptyInput("Enter Vehicle model name: ")
	color = userInput.getNonEmptyInput("Enter Vehicle color: ")

	# TODO: Must validate, return invalid vehicle type
	typeId = userInput.getValidatedInput("Enter Vehicle type: ", 
		lambda result: isValidVehicleType(conn, result))

	year = userInput.getIntegerInput("Enter Vehicle year: ")

	owner_id = input("Enter Owner SIN: ")
	primaryOwner = userInput.getYesNoInput("Primary Owner (y) or (n): ")

	print("All info got!")
	# TODO connect to oracle and pass information in

# Set up vehicle registration 
def setupVehicleReg(conn):
	try:
		setupVehicleRegImpl(conn)
	except KeyboardInterrupt:
		print("\n\n<<< Canceled add >>>\n")
		return

def main():
	setupVehicleReg("test")
if __name__ == "__main__":
	main()

# Requires oracle login string
# Gets owners SIN and Vehicle ID

import cx_Oracle
import sys
import userInput

def isValidSerialNo(conn, serial):
	# Must not be empty
	if serial == "":
		return "Serial number must not be empty"

	# Serial Must not exist yet
	curs = conn.cursor()
	curs.execute("SELECT count(*) FROM vehicle WHERE serial_no = '%s'" % serial)
	if curs.fetchall()[0][0] != 0:
		return "Serial number already registered"

	return True


def isValidVehicleType(conn, vtype):
	curs = conn.cursor()
	curs.execute("SELECT count(*) FROM vehicle_type WHERE type = '%s'" % vtype)
	if curs.fetchall()[0][0] > 0:
		return True
	else:
		return "Not a valid vehicle type"
	

def setupVehicleRegImpl(conn):
	print("\nNew Vehicle Registration\n")

	# Serial number (must be unique)
	serial_no = userInput.getValidatedInput("Enter Vehicle serial #: ",
		lambda result: isValidSerialNo(conn, result))

	# Validated vehicle type (type must exist)
	typeId = userInput.getValidatedInput("Enter Vehicle type: ", 
		lambda result: isValidVehicleType(conn, result))

	# Other easy inputs
	maker = userInput.getNonEmptyInput("Enter Vehicle maker name: ")
	model = userInput.getNonEmptyInput("Enter Vehicle model name: ")
	color = userInput.getNonEmptyInput("Enter Vehicle color: ")

	# TODO: Validate further
	year = userInput.getIntegerInput("Enter Vehicle year: ")

	# All good insert the item
	curs = conn.cursor()
	curs.execute("INSERT INTO vehicle VALUES "
		"('%s', '%s', '%s', );")

	# Owners, repeat until enters q. If driver doesnt exist return message and ask to add to database
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

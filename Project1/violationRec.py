# Issue a ticket and record violation 
import cx_Oracle
import datetime
import person
import sys
import userInput
import newVehReg
import vehicle

# isvalidvehicletype
# checks if valid vehicle type
def isValidVehicleType(conn, vtype):
	curs = conn.cursor()
	curs.execute("SELECT count(*) FROM vehicle_type WHERE name = '%s'" % vtype)
	if curs.fetchall()[0][0] > 0:
		return True
	else:
		return "Not a valid vehicle type"
	
# TODO, add a way to auto include primary driver of a vehicle instead of taking input

# is valid serial no
# checks if vehicle has valid serial number
def isValidSerialNo(conn, serial):
	if vehicle.checkExists(conn, serial):
		return True 
	else:
		return "Serial Number not registered"

# is valid ticket type
# Checks if ticket's type is valid
def isValidTicketType(conn, tType):
	curs = conn.cursor()
	curs.execute("SELECT count(*) FROM ticket_type WHERE vtype = '%s'" % tType)
	if curs.fetchall()[0][0] > 0:
		return True
	else:
		return "Not a valid ticket type"

# Check ticket exists
# Checks if ticketID already exists 
def checkTicExists(conn, ticketID):
	curs = conn.cursor()
	curs.execute("SELECT count(*) FROM ticket WHERE ticket_no = '%d'" % ticketID)
	return curs.fetchall()[0][0] > 0

# isvalidTicketID
# Queries to make sure ticketID does not exist
def isValidTicketID(conn, ticketID):
	if not checkTicExists(conn, ticketID):
		return True
	else:
		return False

#
def isValidViolator(conn, vehicle, sin):
	if sin == "":
		if vehicle.getPrimaryOwner(conn, vehicle):
			return True
		else:
			return "Vehicle has no primary owner, must specify an owner"
	else:
		if person.checkExists(conn, sin):
			return True
		else:
			return "That person is not registered"


#
#def isValidOfficer(conn, sin):
	



# recordTicket
# Main fuction to record a violation
# Collects User inputs validating the ones that need to be checked
# Once everything is correct adds to ticket
# Note: Once you start process, there is not way to get out
def recordTicketImpl(conn):
	# First get VIN
	vin = userInput.getValidatedInput(
		"Enter serial no of vehicle recieving violation:",
		lambda result: isValidSerialNo(conn, result))

	# Now, get the violator, or none
	violator_sin = userInput.getValidatedInput(
		"Enter the violator SIN (leave blank to default to a primary owner): ",
		lambda result: isValidViolator(conn, vin, result))
	
	# Get the officer
	officer_sin = userInput.getValidatedInput(
		"Enter the recording officer SIN: ",
		lambda result: person.checkExists(conn, result))


	while validationCheck == 1:
		officerID = userInput.getIntegerInput("Officer ID: ")
		try:
			if not person.checkExists(conn, officerID):
				print("Incorrect Sin")
			else:
				validationCheck = 2
		except:
			print("SIN number not in database")

	#TODO, same violation check for each necessary variable
	
	if validationCheck == 2:
		# Vehicle ID is vehicle serial number
		serial_no = userInput.getValidatedInput("Enter vehicle serial #: ",
			lambda result: isValidSerialNo(conn, result))

		# Vtype is from ticket type 
		vtype = userInput.getValidatedInput("Enter ticket type: ",
			lambda result: isValidTicketType(conn, result))

		# Format the current date 
		ticketDate = datetime.datetime.now()
		ticketDate = "%s/%s/%s" % (ticketDate.year, ticketDate.month, ticketDate.day)
		validationCheck = 3
	else:
		pass

	# Make Sure Ticket ID is unique
	while validationCheck == 3:
		ticketType = userInput.getIntegerInput("Enter ticket ID: ")
		validTicCheck = isValidTicketID(conn, ticketType)
		if validTicCheck:
			validationCheck = 4
		else:
			print("Ticket ID used")
	while validationCheck == 4:
		ticketPlace = input("Where the ticket occurred: ") 
		description = input("Description for ticket: ")
		validationCheck = 5

	if validationCheck == 5:
		curs = conn.cursor()
		curs.execute("INSERT INTO ticket VALUES "
			"('%d', '%s', '%s', '%s', '%s', to_date('%s', 'yyyy/mm/dd'), '%s', '%s')" %
			(ticketType, violatID, serial_no, officerID, vtype, ticketDate, ticketPlace, description))
		conn.commit()
		print("<<< Ticket Registered >>>\n") 
	else:
		print("<<< Ticket Canceled >>>\n") 


def recordTicket(conn):
	try:
		recordTicketImpl(conn)
	except KeyboardInterrupt:
		print("\n\n<<< Canceled Adding Violation Record >>>\n\n")

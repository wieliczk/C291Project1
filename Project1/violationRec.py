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
	curs.execute("SELECT count(*) FROM ticket WHERE ticket_no = %d" % ticketID)
	return curs.fetchall()[0][0] > 0

# isvalidTicketID
# Queries to make sure ticketID does not exist
def isValidTicketID(conn, ticketID):
	if not checkTicExists(conn, ticketID):
		return True
	else:
		return False

#
def isValidViolator(conn, vin, sin):
	if sin == "":
		if vehicle.getPrimaryOwner(conn, vin):
			return True
		else:
			return "Vehicle has no primary owner, must specify an owner"
	else:
		if person.checkExists(conn, sin):
			return True
		else:
			return "That person is not registered"


#
def isValidOfficer(conn, sin):
	if person.checkExists(conn, sin):
		return True
	else:
		return "That officer does not exist"	


#
def getNextTicketNo(conn):
	curs = conn.cursor()
	ticket_no = curs.execute("SELECT max(ticket_no)+1 FROM ticket").fetchall()[0][0]
	if ticket_no == None:
		ticket_no = 0
	return ticket_no


# recordTicket
# Main fuction to record a violation
# Collects User inputs validating the ones that need to be checked
# Once everything is correct adds to ticket
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
		lambda result: isValidOfficer(conn, result))

	# Get the ticket type
	vtype = userInput.getValidatedInput(
		"Enter the type of violation: ",
		lambda result: isValidTicketType(conn, result))

	# Get the date
	vdate = userInput.getDateInput(
		"Enter the violation date (yyyy/mm/dd): ")

	# Get the place
	location = input("Enter the place of violation (max 10 chars): ")
	if len(location) > 10:
		print("Warning: Input was greater than 10 characters, truncating.")
	location = location[:10]

	# Get the description
	desc = input("Enter a description of the violation (max 1024 chars): ")
	if len(desc) > 1024:
		print("Warning: Input was greater than 1024 characters, truncating.")
	desc = desc[:1024]

	# Get ticket no
	ticket_no = getNextTicketNo(conn)
	
	# Do the insert
	curs = conn.cursor()
	curs.execute("INSERT INTO ticket VALUES "
		"('%d', '%s', '%s', '%s', '%s', to_date('%s', 'yyyy/mm/dd'), '%s', '%s')" %
		(ticket_no, violator_sin, vin, officer_sin, vtype, vdate, location, desc))
	conn.commit()

	print("<<< Ticket Registered >>>\n") 


def recordTicket(conn):
	try:
		recordTicketImpl(conn)
	except KeyboardInterrupt:
		print("\n\n<<< Canceled Adding Violation Record >>>\n\n")

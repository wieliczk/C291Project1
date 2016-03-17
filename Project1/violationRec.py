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

# recordTicket
# Main fuction to record a violation
# Collects User inputs validating the ones that need to be checked
# Once everything is correct adds to ticket
# Note: Once you start process, there is not way to get out
def recordTicket(conn):
	# Violator id and office id are SIN's
	validationCheck =0
	while validationCheck == 0:
		violatID = userInput.getIntegerInput("Violator ID (00 to quit): ")
		try:
			if not person.checkExists(conn, violatID):
				if violatID == 00:
					validationCheck = 9
				else:
					print("Incorrect Sin")
				
			else:
				validationCheck = 1
		except:
			print("SIN number not in database")

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

def main():
	recordTicket("Test")

if __name__ == "__main__":
	main()


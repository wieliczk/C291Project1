# Issue a ticket and record violation 
import cx_Oracle
import datetime


def isValidVehicleType(conn, vtype):
	curs = conn.cursor()
	curs.execute("SELECT count(*) FROM vehicle_type WHERE type = '%s'" % vtype)
	if curs.fetchall()[0][0] > 0:
		return True
	else:
		return "Not a valid vehicle type"
	
# TODO, add a way to auto include primary driver of a vehicle instead of taking input

def recordTicket(logString):
	# Violator id and office id are SIN's
	validationCheck =0
	while validationCheck == 0:
		violatID = input("Violator ID: ")
		try:
			#query if violatID is in SIN numbers
			validationCheck = 1
		except:
			print("SIN number not in database")

	#TODO, same violation check for each necessary variable
	#Is officer ID a SIN number

	officeID = input("Officer ID: ")
	
	# Vehicle ID is vehicle serial number
	vehicleID = input("Vehicle Serial Number: ")
	
	# Vtype is from ticket type 
	vtype = input("Ticket type: ")
	ticketDate = datetime.date.today()
	checks = 0
	while checks == 0:
		try:
			ticketID = int(input("Create Ticket ID: "))
			checks = 1

		except:
			print("Enter Int\n")
	ticketPlace = input("Where the ticket occurred: ") 
	description = input("Description for ticket: ")
	# TODO add oracle queries 
	# TODO make sure ticket ID is unique
	

def main():
	recordTicket("Test")

if __name__ == "__main__":
	main()


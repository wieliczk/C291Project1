# Issue a ticket and record violation 
import cx_Oracle
import datetime

def recordTicket(logString):
	# Violator id and office id are SIN's
	violatID = input("Violator ID: ")
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

def main():
	recordTicket("Test")

if __name__ == "__main__":
	main()


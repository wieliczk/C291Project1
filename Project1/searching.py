# Deals with searching 
# 3 options
# 1) use licence or name to get information
# 2) use licence or sin to get all violations 
# 3) Use vehicle serial number to see all violations its a part of 

import cx_Oracle
import sys
import userInput
import person
import licence
import vehicle


def searchOption(conn):
	intChoice = getChoice()
	if intChoice == 1:
		personalInfo(conn)
	elif intChoice == 2:
		violationRecords(conn)
	else:
		vehicleHist(conn)  


def getChoice():
	print("Choose option:\n" \
	      "(1): Get personal information by licence or name\n" \
	      "(2): List violation records by licence or SIN\n" \
	      "(3): List vehicle history by vehicle serial number\n")
	checks = 1
	while checks == 1:
		try:
			chooses = int(input("Enter number: "))
			if chooses in [1,2,3]:
				checks = 0
			else:
				print("Incorrect Number\n")
		except:
			print("Invalid Entry\n")
	return chooses


#search for person info by name
def personalByName(conn, name):
	curs = conn.cursor()
	curs.execute(
		"SELECT p.sin, p.name, licence_no, p.addr, p.birthday, d.class, d.expiring_date "
		"FROM people p, drive_licence d WHERE p.sin = d.sin AND lower(p.name) = '%s'" % 
		name)
	row = curs.fetchone()
	if not row:
		print("No matching results")
		return 0
	while row:
		print("%s:" % row[1])
		print(" |  Licence#: %s" % row[2])
		print(" |  Address: %s" % row[3])
		print(" |  Birthday: %s" % row[4])
		print(" |  Driving Class: %s" % row[5])
		print(" |  Expiry Date: %s" % row[6])
		print(" |  Conditions:")
		curs2 = conn.cursor()
		curs2.execute(
			"SELECT description FROM driving_condition, restriction "
			"WHERE c_id = r_id AND licence_no = '%s'" % row[2])
		for cond in curs2.fetchall():
			print(" |      %s" % cond[0])
		print(" \\-------")
		row  = curs.fetchone()
	return 0
	
		
#search for person info by name
def personalByLicence(conn, licence_no):
	curs = conn.cursor()
	curs.execute(
		"SELECT p.sin, p.name, licence_no, p.addr, p.birthday, d.class, d.expiring_date "
		"FROM people p, drive_licence d WHERE p.sin = d.sin AND lower(d.licence_no) = '%s'" % 
		licence_no.lower())
	row = curs.fetchone()
	if not row:
		print("No matching results")
		return 0
	while row:
		print("%s:" % row[1])
		print(" |  Licence#: %s" % row[2])
		print(" |  Address: %s" % row[3])
		print(" |  Birthday: %s" % row[4])
		print(" |  Driving Class: %s" % row[5])
		print(" |  Expiry Date: %s" % row[6])
		print(" |  Conditions:")
		curs2 = conn.cursor()
		curs2.execute(
			"SELECT description FROM driving_condition, restriction "
			"WHERE c_id = r_id AND licence_no = '%s'" % row[2])
		for cond in curs2.fetchall():
			print(" |      %s" % cond[0])
		print(" \\-------")
		row  = curs.fetchone()
	return 0
	

#search for violation info by SIN
def violationBySin(conn, sin):
	curs = conn.cursor()
	curs.execute(
		"SELECT name, sin, ticket_no, violator_no, vtype, vdate, office_no, descriptions, place, vehicle_id "
		" FROM ticket, people WHERE violator_no=sin and sin='%s'" % sin)
	row = curs.fetchone()
	#check if theres no row to fetch aka empty results
	if not row:
		print("Person has received no violation tickets")
		return 0
	#If first result, print until none left
	print("Violations for %s (SIN: %s):" % (row[0].strip(), sin.strip()))
	while row:
		print("    Ticket #%s for %s by vehicle #%s\n        Awarded on %s in %s by officer %s\n        Description: %s" %
			(row[2], row[4].strip(), row[9], row[5], row[8], row[6], row[7]))
		row  = curs.fetchone()
	return 0


#search for violation info by licence no
def violationByLicence(conn, licence_no):
	curs = conn.cursor()
	curs.execute(
		"SELECT p.name, p.sin, ticket_no, violator_no, vtype, vdate, office_no, descriptions, place, vehicle_id "
		" FROM ticket, people p, drive_licence d WHERE p.sin = d.sin AND violator_no = p.sin and lower(licence_no) = '%s'" % 
		licence_no.lower())
	row = curs.fetchone()
	#check if theres no row to fetch aka empty results
	if not row:
		print("Person has received no violation tickets")
		return 0
	#If first result, print until none left
	print("Violations for %s (SIN: %s, Licence#: %s):" % (row[0].strip(), row[1].strip(), licence_no.strip()))
	while row:
		print("    Ticket #%s for %s by vehicle #%s\n        Awarded on %s in %s by officer %s\n        Description: %s" %
			(row[2], row[4].strip(), row[9], row[5], row[8], row[6], row[7]))
		row  = curs.fetchone()
	return 0


#vehicle history searching given vehicle serial
def vehicleHistSearch(conn, vehicleID):
	print("Vehicle %s:" % vehicleID)
	curs = conn.cursor()
	#counts number of tickets vehicle has received
	curs.execute("SELECT count(ticket_no) FROM ticket WHERE vehicle_id='%s'" %vehicleID)
	row = curs.fetchone()
	if row:
		print(" |  Has received %s tickets" % row)

	#counts number of sales cars been involved in
	curs.execute("SELECT count(transaction_id) from auto_sale WHERE vehicle_id='%s'" %vehicleID)
	row = curs.fetchone()
	print (" |  And been involved in %s transactions" % row)
	if row[0] > 0:
	#finds average sale price for vehicle only if its been in a sale
		curs.execute("SELECT avg(price) from auto_sale where vehicle_id='%s'" % vehicleID)
		row = curs.fetchone()
		print(" |  With an average sale price of $%s over those transactions" % row[0])
		print(" \\----------\n")
		return 0
	return 0



def personalInfo(conn):
	print("Personal Info\n")
	#lets us repeat searches until user stops us
	quitcheck = 1
	while quitcheck == 1:
		try:
			#chooses lets user decide to search by username or licence number
			chooses = int(input("(1): Search by name\n(2): Search by licence\n(3): Quit\n"))
			print("chooses: %d" % chooses)
			if chooses == 1:
				searchBy = str(input("Enter name to search: "))
				searchBy = searchBy.lower()
				personalByName(conn, searchBy)
				# TODO check if we need to do more precise query to get diff people with same name or less info
				# TODO does it matter if the result has their licence_no included? prob not
				searchBy = None #wipes stored value for searchBy
				chooses == None #wipes the previous entry for chooses

			if chooses == 2:
				while chooses == 2:
					try:
						searchBy = input("Enter licence number to search: ")
						if licence.checkExists(conn, searchBy):
							personalByLicence(conn, searchBy)	
						else:
							print("Licence number not registered")
						searchBy = None
						chooses = None
						break
					except ValueError:
						print("Not a valid number")

			if chooses == 3:
				quitcheck = 0
				break

		except ValueError:
			print("Invalid entry")

		except KeyboardInterrupt:
			break



def violationRecords(conn):
	print("Violation Records\n")
	quitcheck = 1
	while quitcheck == 1:
		try:
			#chooses lets user decide to search by username or licence number
			chooses = int(input("(1): Search by SIN\n(2): Search by licence\n(3): Quit\n"))
			if chooses == 1:
				while chooses == 1:
					try:
						searchBy = input("Enter SIN number to search: ")
						if person.checkExists(conn, searchBy):
							violationBySin(conn, searchBy)
						else:
							print("Sin number not registered")
						searchBy = None
						chooses = None
						break
					except ValueError:
						print("Not a valid number")

			if chooses == 2:
				while chooses == 2:
					try:
						searchBy = input("Enter licence number to search: ")
						if licence.checkExists(conn, searchBy):
							violationByLicence(conn, searchBy)				
						else:
							print("Licence number not registered")
						searchBy = None
						chooses = None
						break
					except ValueError:
						print("Not a valid number")
			elif chooses == 3:
				quitcheck = 0
				break

		except ValueError:
			print("Invalid entry")

		except KeyboardInterrupt:
			break
	
	

def vehicleHist(conn):
	print("Vehicle History\n")
	# TODO query using vehicle serial number
	quitcheck = 1
	while quitcheck == 1:
		try:
			#chooses lets user decide to search or quit
			chooses = int(input("(1): Search by Vehicle ID\n(2): Quit\n"))
			if chooses == 1:
				while chooses == 1:
					try:
						searchBy = str(input("Enter Vehicle ID to search: "))
						if vehicle.checkExists(conn, searchBy):
							vehicleHistSearch(conn, searchBy)
						else:
							print("Vehicle not registered")
							continue
						searchBy = None
						chooses = None
						break
					except KeyboardInterrupt:
						print("\n")
						break

			elif chooses == 2:
				quitcheck = 0

			else:
				print("Not a valid choice")

		except ValueError:
			print("Not a valid choice")

		except KeyboardInterrupt:
			break

def main():
	searchOption("Test")

if __name__ == "__main__":
	main()

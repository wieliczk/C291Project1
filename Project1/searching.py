# Deals with searching 
# 3 options
# 1) use licence or name to get information
# 2) use licence or sin to get all violations 
# 3) Use vehicle serial number to see all violations its a part of 

import cx_Oracle
import sys
import userInput

def searchOption(logString):
	intChoice = getChoice()
	if intChoice == 1:
		personalInfo(logString)
	elif intChoice == 2:
		violationRecords(logString)
	else:
		vehicleHist(logString)  


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

	# TODO query using licence no

#search for person info by name
def personalByName(conn, name):
	curs = conn.cursor()
	curs.execute("SELECT * FROM people, drive_licence WHERE name like '%%%s%%';" % name)
	if curs.fetchall()[0][0] > 0:
		for row in curs.fetchall():
			print(row)
	else:
		return "No matching results"

#search for person info by licence
def personalByLicence(conn, licence):
	curs = conn.cursor()
	curs.execute("SELECT * FROM people, drive_licence WHERE people.sin=drive_licence.sin and licence_no = '%s';" %licence)
	if curs.fetchall()[0][0] > 0:
		for row in curs.fetchall():
			print (row)
	else:
		return "No matching results"

#search for violation info by SIN
def violationBySin(conn, sin):
	curs=conn.cursor()
	curs.execute("SELECT name, sin, ticket_no, licence_no, vtype FROM ticket, people WHERE violator_no=sin and sin='%s';" % sin)
	if curs.fetchall()[0][0] > 0:
		for row in curs.fetchall():
			print (row)
	else:
		return "No matching results"

#search for violation info by licence
def violationByLicence(conn, licence):
	curs=conn.cursor()
	curs.execute("select name, sin, ticket_no, licence_no, vtype FROM ticket, people, drive_licence where peolpe.sin=drive_licence.sin and people.sin=violator_no and licence_no='%s';" % licence)
	if curs.fetchall()[0][0] > 0:
		for row in curs.fetchall():
			print(row)
	else:
		return "No matching results"


#vehicle history searching given vehicle serial
def vehicleHistSearch(conn, vehicleID):
	curs=conn.cursor()
	#counts number of tickets vehicle has received
	curs.execute("SELECT count(ticket_no) FROM ticket WHERE vehicle_id='%s';" %vehicleID)
	if curs.fetchone() > 0:
		print("Vehicle has received '%s' tickets\n" % curs.fetchone)
	else:
		print("Vehicle has received no tickets\n")

	#counts number of sales cars been involved in
	curs.execute("SELECT count(transaction_id) from auto_sale WHERE vehicle_id='%s';" %vehicleID)
	if curs.fetchone() > 0:
		print ("Car involved in '%s' transactions" %curs.fetchone())
	else:
		print ("Not involved in any sales")
		return True #ends vehicle search, no sales means no average
	#finds average sale price for vehicle
	curs.execute("SELECT avg(price) from auto_sale where vehicle_id='%s';" %vehicleID)
	print(curs.fetchone())





def personalInfo(logString):
	print("Personal Info\n")
	#lets us repeat searches until user stops us
	quitcheck = 1
	while quitcheck == 1:
		try:
			#chooses lets user decide to search by username or licence number
			chooses = int(input("(1): Search by name\n(2): Search by licence\n(3): Quit\n"))
			if chooses == 1:
				searchBy = str(input(("Enter name to search: \n")))
				searchBy=searchBy.lower()
				personalByName(conn, searchBy)
				# TODO check if we need to do more precise query to get diff people with same name or less info
				# TODO does it matter if the result has their licence_no included? prob not
				searchBy = None #wipes stored value for searchBy
				chooses == None #wipes the previous entry for chooses
				


			if chooses == 2:
				while chooses == 2:
					try:
						searchBy = int(input(("Enter licence number to search: ")))
						personalByLicence(conn, searchBy)
						searchBy = None
						chooses = None
						break
					except Exception as e:
						print(e)
						print("Not a valid number")

			if chooses == 3:
				quitcheck = 0
				break

		except Exception as e:
			print(e)
			print("Invalid entry")
	


	






def violationRecords(logString):
	print("Violation Records\n")
	quitcheck = 1
	while quitcheck == 1:
		try:
			#chooses lets user decide to search by username or licence number
			chooses = int(input("(1): Search by SIN\n(2): Search by licence\n(3): Quit\n"))
			if chooses == 1:
				while chooses == 1:
					try:
						searchBy = int(input(("Enter SIN number to search: ")))
						violationBySin(conn, searchBy)
						searchBy = None
						chooses = None
						break
					except ValueError:
						print("Not a valid number")

			if chooses == 2:
				while chooses == 2:
					try:
						searchBy = int(input(("Enter licence number to search: ")))
						violationByLicence(conn, licence)				
						searchBy = None
						chooses = None
						break
					except ValueError:
						print("Not a valid number")
			elif chooses == 3:
				quitcheck = 0
				break
		except:
			print("Invalid entry")
	
	

def vehicleHist(logString):
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
						searchBy = int(input(("Enter Vehicle ID to search: ")))
						vehicleHistSearch(conn, searchBy)
						searchBy = None
						chooses = None
						break
					except ValueError:
						print("Not a valid number")

			elif chooses == 2:
				quitcheck = 0

		except:
				print("Not a valid choice")

def main():
	searchOption("Test")

if __name__ == "__main__":
	main()

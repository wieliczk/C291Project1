# Deals with searching 
# 3 options
# 1) use licence or name to get information
# 2) use licence or sin to get all violations 
# 3) Use vehicle serial number to see all violations its a part of 

import cx_Oracle


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
				# TODO check if we need to do more precise query to get diff people with same name or less info
				#curs = connection.cursor()
				#curs.execute("SELECT * from people, drive_licence WHERE name like '%%%s%%';" % searchBy)
				#Like searches for all names with subsets: aka Joa A, Joe B, Joe K
				#for row in curs:
					#print the resulting rows
				#	print(row)
				#curs.close()
				# TODO does it matter if the result has their licence_no included? prob not
				
				searchBy = None #wipes stored value for searchBy
				chooses == None #wipes the previous entry for chooses
				


			if chooses == 2:
				while chooses == 2:
					try:
						searchBy = int(input(("Enter licence number to search: ")))
						#curs = connection.cursor()
						#curs.execute("SELECT * from people, drive_licence WHERE people.sin=drive_licence.sin and licence_no='%s';" % searchBy)
						#for row in curs:
							#print(row)
						#curs.close()
						searchBy = None
						chooses = None
						break
					except:
						print("Not a valid number")

			if chooses == 3:
				quitcheck = 0
				break

		except Exception as e:
			print(e)
			#print("Invalid entry")
	


	






def violationRecords(logString):
	print("Violation Records\n")
	# TODO query using licence_no or SIN
	quitcheck = 1
	while quitcheck == 1:
		try:
			#chooses lets user decide to search by username or licence number
			chooses = int(input("(1): Search by SIN\n(2): Search by licence\n(3): Quit\n"))
			if chooses == 1:
				while chooses == 1:
					try:
						searchBy = int(input(("Enter SIN number to search: ")))
						#curs = connection.cursor()
						#curs.execute("select name, sin, ticket_no from ticket, people where violator_no=sin and sin='%s';" % searchBy)
						#for row in curs:
							#print(row)
						#curs.close()
						searchBy = None
						chooses = None
						break
					except:
						print("Not a valid number")

			if chooses == 2:
				while chooses == 2:
					try:
						searchBy = int(input(("Enter licence number to search: ")))
						#curs = connection.cursor()
						#curs.execute("select name, ticket_no, licence_no from ticket, people, drive_licence where peolpe.sin=drive_licence.sin and people.sin=violator_no and licence_no='%s';" % searchBy)
						#for row in curs:
							#print(row)
						#curs.close()						
						searchBy = None
						chooses = None
						break
					except:
						print("Not a valid number")
			elif chooses == 3:
				quitcheck = 0
				break
		except:
			print("Invalid entry")
	


			elif chooses == 2:
				while TRUE:
					try:
						searchBy = int(input(("Enter licence number to search: ")))
						# TODO query using the searchBy
						
						searchBy = None
						chooses = None
						break
					except:
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
						#curs = connection.cursor()
						#curs.execute(='%s';" % searchBy)
						# TODO select count(number of autosales) where vehicle_id=serial_no
						# TODO select count(number of violations) where serial_no=vehicle_id
						# TODO select avg of auto_sale.price
						#for row in curs:
							#print(row)
						#curs.close()						
						searchBy = None
						chooses = None
						break
					except:
						print("Not a valid number")

			elif chooses == 2:
				quitcheck = 0

		except:
				print("Not a valid choice")

def main():
	searchOption("Test")

if __name__ == "__main__":
	main()

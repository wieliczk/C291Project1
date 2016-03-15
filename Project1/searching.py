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


	pass
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
			chooses = int(input("(1): Search by name\n(2): Search by licence\n(3)Quit"))
			if chooses == 1:
				searchBy = str(input(("Enter name to search: ")))
				# TODO query using the searchBy

				searchBy = None #wipes stored value for searchBy
				chooses == None #wipes the previous entry for chooses
				break


			elif chooses == 2:
				while chooses == 2:
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
	


	






def violationRecords(logString):
	print("Violation Records\n")
	# TODO query using licence_no or SIN
	quitcheck = 1
		while quitcheck == 1:
			try:
				#chooses lets user decide to search by username or licence number
				chooses = int(input("(1): Search by SIN\n(2): Search by licence\n(3)Quit"))
				if chooses == 1:
					while chooses == 1:
						try:
							searchBy = int(input(("Enter licence number to search: ")))
							# TODO query using the SearchBy
							searchBy = None
							chooses = None
							break
						except:
							print("Not a valid number")


				if chooses == 2:
					while chooses == 2:
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
				chooses = int(input("(1): Search by Vehicle ID\n(2): Quit"))
				if chooses == 1:
					while chooses == 1:
						try:
							searchBy = int(input(("Enter Vehicle ID to search: ")))
							# TODO query using the searchBy
						
							searchBy = None
							chooses = None
							break
						except:
							print("Not a valid number")


				elif chooses == 2:
					quitcheck = 0





def main():
	searchOption("Test")

if __name__ == "__main__":
	main()

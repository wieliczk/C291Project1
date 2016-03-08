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

def personalInfo(logString):
	print("Personal Info\n")
	# TODO query using licence_no or name

def violationRecords(logString):
	print("Violation Records\n")
	# TODO query using licence_no or SIN

def vehicleHist(logString):
	print("Vehicle History\n")
	# TODO query using vehicle serial number

def main():
	searchOption("Test")

if __name__ == "__main__":
	main()

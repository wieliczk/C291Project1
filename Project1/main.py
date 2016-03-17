# Test for project 1

import sys
import cx_Oracle 
import getpass
# Python File that sets up Oracle
import OracleSetup
# Python Files that handle each option
import newVehReg
import newDriver
import autoTran
import violationRec
import searching

# Ask the user to choose one of the main menu actions available
def chooseMainMenuOption():
	# User chooses which option
	print("(1): New Vehicle Registration \n(2): Driver Licence Registration  \n" \
		  "(3): Auto Transaction \n(4): Violation Record \n" \
		  "(5): Search \n")
	chooses = 0
	while chooses == 0:
		try:
			chosen = input("Choose a number or 'q' to quit: ")
			if chosen == "q":
				break
			else:
				chosen = int(chosen)
			while chosen not in [1,2,3,4,5]:
				print("Invalid")
				chosen = input("Choose a number: ")
				if chosen == "q":
					break
				else:
					chosen = int(chosen)
			chooses = 1
		except KeyboardInterrupt:
			# User ctrl+Ced, interpret as exit
			print("\n")
			return "q"
		except:
			print("Incorrect")
	return chosen


# Main function
def main():
	# Gets correct login as corrlog
	connection = OracleSetup.connectOracle()

	# Main choice loop (until q "quit" is chosen)
	while True:
		# Get the choice and dispatch to the appropriate subprogram
		intchose = chooseMainMenuOption()
		if intchose == "q":
			break # q -> break out of main loop, quitting
		elif intchose == 1:
			newVehReg.setupVehicleReg(connection)
		elif intchose == 2:
			newDriver.newDriver(connection)		
		elif intchose == 3:
			autoTran.performTransaction(connection)
		elif intchose == 4: 
			violationRec.recordTicket(connection)
		else:
			searching.searchOption(connection)
	
	# Done main loop	
	sys.exit()


# Main dispatcher
if __name__ == "__main__":
	main()
		

	

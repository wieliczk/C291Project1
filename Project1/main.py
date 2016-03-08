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

def main():
	# Gets correct login as corrlog
	conAct, corrlog = OracleSetup.connectOracle()
	while conAct == 0:
		print("Failed login")
		conAct = OracleSetup.connectOracle()
	isRunning = 1
	while isRunning == 1:
		# Gets correct int input
		intchose = OracleSetup.controlOptions()
		# Creates loop until q is hit
		if intchose == "q":
			sys.exit()
		elif intchose == 1:
			newVehReg.setupVehicleReg(corrlog)
		elif intchose == 2:
			newDriver.setupDriver(corrlog)		
		elif intchose == 3:
			autoTran.autoTrans(corrlog)
		elif intchose == 4: 
			violationRec.recordTicket(corrlog)
		else:
			searching.searchOption(corrlog)
		# From Here program needs the 5 options.
if __name__ == "__main__":
	main()
		

	

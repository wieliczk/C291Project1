# Test for project 1

import sys
import cx_Oracle 
import getpass
# Python File that sets up Oracle
import OracleSetup
# Python File that handles vehcile Reg
import newVehReg
import newDriver

def main():
	# Gets correct login
	conAct, corrlog = OracleSetup.connectOracle()
	while conAct == 0:
		print("Failed login")
		conAct = OracleSetup.connectOracle()
	# Gets correct int input 
	intchose = OracleSetup.controlOptions()
	if intchose == "q":
		sys.exit()
	elif intchose == 1:
		newVehReg.setupVehicleReg(conAct)
	elif intchose == 2:
		newDriver.setupDriver(conAct)		
	else:
		print("Need to add more") 
	
	# From Here program needs the 5 options.
	
if __name__ == "__main__":
	main()
		

	

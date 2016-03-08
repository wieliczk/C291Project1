# Requires oracle login string
# Gets owners SIN and Vehicle ID

import cx_Oracle
import sys

def setupVehicleReg(loginString):
	print("\nNew Vehicle Registration\n")
	serial_no = input("Enter Vehicle serial #: ")
	maker = input("Enter Vehicle maker name: ")
	model = input("Enter Vehicle model name: ")
	color = input("Enter Vehicle color: ")
	typeOfCar = input("Enter vehicle type: ")
	checks = 0
	while checks == 0:
		try:
			year = int(input("Enter Vehicle year: "))
			checks = 2
			while checks == 2:
				try:
					type_id = int(input("Vehicle type_id: "))
					checks = 1
				except: 
					print("Improper Enter, enter a number" )
		except:
			print("Improper Entry, enter a number: ")
	owner_id = input("Enter Owner SIN: ")
	checks = 0
	while checks == 0:
		primaryOwn = input("Primary Owner (y) or (n): ")
		if len(primaryOwn) == 1 and primaryOwn in ["y","n","Y","N"]:
			checks = 1
		else:
			print("Invalid input")
	print("All info got!")
	# TODO connect to orcale and pass information in

def main():
	setupVehicleReg("test")
if __name__ == "__main__":
	main()

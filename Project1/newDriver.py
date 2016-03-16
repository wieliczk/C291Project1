import sys
import cx_Oracle
import datetime
import time
import person
import vehicle
import licence

# This component is used to record the information 
# needed to issuing a drive licence, including the personal 
# information and a picture for the driver. You may assume that all 
# the image files are stored in a local disk system.

# Check that a licence number is valid
def isLicenceNumberValid(conn, number):
	# Is it nonempty
	if number == "":
		return "No licence number entered"

	# Does it already exist?
	if licence.checkExists(number):
		return "Licence number already exists"

	return True


# Does a file contain a photo?
def isValidPhotoFile(fileName):
	try:
		open(fileName, 'r')
		return True
	except FileNotFoundError:
		return "File does not exist"


# Licence a new driver
def newDriverImpl(conn):
	# Get the registrant
	regist_sin = ""
	while True:
		regist_sin = userInput.getNonEmptyInput("Registrant SIN: ")
		if not person.checkExists(conn, regist_sin):
			shouldRegister = userInput.getYesNoInput(
				"Registrant not in database, register them? (y) or (n): ")
			if shouldRegister:
				didRegister = person.register(conn, regist_sin)
				if didRegister:
					break
				else:
					continue
			else:
				continue

	# Licence no
	licence_no = userInput.getValidatedInput("New Licence Number: ",
		lambda result: isLicenceNumberValid(conn, result))

	# Class
	licence_class = userInput.getNonEmptyInput("Class: ")

	# Photo
	photo = userInput.getValidatedInput("Photo file: ",
		lambda result: isValidPhotoFile(result))

	# Issue and Expiry dates
	issue_date = userInput.getDateInput("Issue Date (yyyy/mm/dd): ")
	expiry_date = userInput.getDateInput("Exiry Date (yyyy/mm/dd): ")

	# Restrictions
	# TODO:

	curs = conn.cursor()

	# Read in the photo data
	photo_data = open(photo, 'rb').read()

	photo_var = curs.var(cx_Oracle.BLOB)
	photo_var.setvalue(0, photo_data)

	curs.execute("INSERT INTO drive_licence VALUES "
		"('%s', '%s', '%s', :photo, to_date('%s', 'yyyy/mm/dd'), to_date('%s', 'yyyy'))" % 
		(licence_no, regist_sin, licence_class, issue_date, expiry_date),
		photo = photo_var)



# 
def newDriver(conn):
	try:
		newDriverImpl(conn)
	except KeyboardInterrupt:
		print("\n\n<<< Canceled Performing Transaction >>>\n")


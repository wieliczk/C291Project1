import sys
import cx_Oracle
import datetime
import time
import person
import vehicle
import licence
import userInput
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
	if licence.checkExists(conn, number):
		return "Licence number already exists"

	return True


# Does a file contain a photo?
def isValidPhotoFile(fileName):
	if fileName == "":
		return True
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
					addDriver(conn, regist_sin)
					break
				else:
					break
		if person.checkExists(conn, regist_sin):
			#checks if person with SIN has a licence already
			hasLicence = person.hasLicence(conn, regist_sin)
			if hasLicence:
				print("Registrant already has a licence\n")
				break
			else:
				addDriver(conn, regist_sin)
				break



#do we need to be able to update existing licences with new types/expiry dates?
#execute to update existing personal licence if required. Only one licence per person (unique constraint in profs).
#curs.execute("update drive_licence SET "
#"licence_no='%s', class='%s', photo='%s', issuing_date= CAST('%s' AS DATETIME), expiring_date= CAST('%s' AS DATETIME) where sin=regist_sin"
# %(licence_no, licence_class, photo_var issue_date, expiry_date )


def addDriver(conn, sin):
	#Licence no
	licence_no = userInput.getValidatedInput("New Licence Number: ",
		lambda result: isLicenceNumberValid(conn, result))

	# Class
	licence_class = userInput.getNonEmptyInput("Class: ")

	# Photo
	photo = userInput.getValidatedInput("Photo file (leave empty if none): ",
		lambda result: isValidPhotoFile(result))
	
	# Issue and Expiry dates
	issue_date = userInput.getDateInput("Issue Date (yyyy/mm/dd): ")
	expiry_date = userInput.getDateInput("Expiry Date (yyyy/mm/dd): ")

	# Restrictions
	restriction_list = []
	while True:
		restrict = userInput.getNonEmptyInput(
			"Add a driving restriction (done if no more): ")

		if restrict.lower() == "done":
			break
		else:
			restriction_list.append(restrict)

	curs = conn.cursor()

	# Save photo if exists
	photo_var = curs.var(cx_Oracle.BLOB)
	if photo != "":		
		photo_data = open(photo, 'rb').read()
		photo_var.setvalue(0, photo_data)

	# Add the licence
	curs.execute("INSERT INTO drive_licence VALUES "
		"('%s', '%s', '%s', :photo, to_date('%s', 'yyyy/mm/dd'), to_date('%s', 'yyyy/mm/dd'))" % 
		(licence_no, sin, licence_class, issue_date, expiry_date),
		photo = photo_var)

	# Add restrictions
	next_condition_id = curs.execute("SELECT max(c_id)+1 FROM driving_condition").fetchall()[0][0]
	if next_condition_id == None:
		next_condition_id = 0
	for restrict in restriction_list:
		curs.execute("INSERT INTO driving_condition VALUES "
			"(%d, '%s')" % (next_condition_id, restrict))
		curs.execute("INSERT INTO restriction VALUES "
			"('%s', %d)" % (licence_no, next_condition_id))
		next_condition_id = next_condition_id + 1

	conn.commit()

	print("<<< Driver Licence Registered >>>\n\n")

# 
def newDriver(conn):
	try:
		newDriverImpl(conn)
	except KeyboardInterrupt:
		print("\n\n<<< Canceled Performing Transaction >>>\n")


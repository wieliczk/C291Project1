
import userInput


# Check if a gender is valid
def isValidGender(gender):
	if gender.lower() in ['m', 'f']:
		return True
	else:
		return "%s is not a valid gender" % gender


# checkExists(conn, sin)
#	Use conn to check if a person with the given sin exists
def checkExists(conn, sin):
	curs = conn.cursor()
	curs.execute("SELECT count(*) FROM people WHERE sin = '%s'" % sin)
	return curs.fetchall()[0][0] > 0


# register(conn, sin)
#	Use conn to register a new person with the given sin and some
#	values to be entered by the user.
#	Returns: True if the user was registered, False if the registration was
#	         canceled by the user.
def register(conn, sin):
	print("Registering person with SIN = %s" % sin)
	try:
		# Get the data fields
		name = userInput.getNonEmptyInput("Name: ")
		height = input("Height: ")
		weight = input("Weight: ")
		eyecolor = input("Eye Color: ")
		haircolor = input("Hair Color: ")
		addr = input("Address: ")
		gender = userInput.getValidatedInput("Gender (m) or (f): ", isValidGender)
		gender = gender.lower()
		birthday = userInput.getDateInput("Birthday (yyyy/mm/dd): ")

		# Do the register
		curs = conn.cursor()
		curs.execute("INSERT INTO people VALUES "
			"('%s', '%s', %s, %s, '%s', '%s', '%s', '%s', to_date('%s', 'yyyy/mm/dd'))" %
			(sin, name, height, weight, eyecolor, haircolor, addr, gender, birthday))
		conn.commit()

		# Done
		print("<<< Person Registered >>>\n\n")
		return True

	except KeyboardInterrupt:
		print("\n<<< Canceled Registering Person >>>\n\n")
		return False


def hasLicence(conn, sin):
	curs = conn.cursor()
	curs.execute("SELECT count(*) FROM people, drive_licence WHERE drive_licence.sin=people.sin and people.sin = '%s'" % sin)
	return curs.fetchall()[0][0] > 0

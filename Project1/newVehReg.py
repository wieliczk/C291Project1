# Requires oracle login string
# Gets owners SIN and Vehicle ID

import cx_Oracle
import sys
import userInput
import person
import vehicle

def isValidSerialNo(conn, serial):
	# Must not be empty
	if serial == "":
		return "Serial number must not be empty"

	# Serial Must not exist yet
	if not vehicle.checkExists(conn, serial):
		return True
	else:
		return "Serial number already registered"


def isValidVehicleType(conn, vtype):
	curs = conn.cursor()
	curs.execute("SELECT count(*) FROM vehicle_type WHERE type = '%s'" % vtype)
	if curs.fetchall()[0][0] > 0:
		return True
	else:
		return "Not a valid vehicle type"


# Get a vehicle type id from a string vehicle type
def convertVehicleTypeToId(conn, vtype):
	curs = conn.cursor()
	curs.execute("SELECT type_id FROM vehicle_type WHERE type = '%s'" % vtype)
	return curs.fetchall()[0][0]


# Does a person own a vehicle already?
def doesPersonOwnVehicle(conn, sin, vin):
	curs = conn.cursor()
	curs.execute("SELECT count(*) FROM owner WHERE owner_id = '%s' AND vehicle_id = '%s'" %
		(sin, vin))
	return curs.fetchall()[0][0] > 0
	

# The actual vehicle registration part
def vehicleRegPart(conn):
	print("\nNew Vehicle Registration\n")

	# Serial number (must be unique)
	serial_no = userInput.getValidatedInput("Enter Vehicle serial #: ",
		lambda result: isValidSerialNo(conn, result))

	# Validated vehicle type (type must exist)
	vtype = userInput.getValidatedInput("Enter Vehicle type: ", 
		lambda result: isValidVehicleType(conn, result))
	typeId = convertVehicleTypeToId(conn, vtype)

	# Other easy inputs
	maker = userInput.getNonEmptyInput("Enter Vehicle maker name: ")
	model = userInput.getNonEmptyInput("Enter Vehicle model name: ")
	color = userInput.getNonEmptyInput("Enter Vehicle color: ")

	# TODO: Maybe validate further
	year = userInput.getIntegerInput("Enter Vehicle year: ")

	# All good insert the item
	curs = conn.cursor()
	curs.execute("INSERT INTO vehicle VALUES "
		"('%s', '%s', '%s', %d, '%s', %d)" %
		(serial_no, maker, model, year, color, typeId))
	conn.commit()

	print("<<< Vehicle Registered >>>\n\n")
	return serial_no


# Add owners to the vehicle
def addOwnersPart(conn, vehicle_serial_no):
	# Primary owner
	hasGotPrimaryOwner = False

	# Owners
	print("Enter the SINs of the vehicle owners:")
	while True:
		# Get the SIN
		owner_id = input("Enter owner SIN (or 'done' if no more): ")

		# No more owners
		if owner_id.lower() == "done":
			break

		# Ensure that the person exists
		if not person.checkExists(conn, owner_id):
			shouldRegister = userInput.getYesNoInput(
				"No person with that SIN exists in the database.\n"
				"Do you want to register them? (y) or (n): ")
			if shouldRegister:
				didRegister = person.register(conn, owner_id)
				if not didRegister:
					continue
			else:
				continue

		# Do they already own the vehicle?
		if doesPersonOwnVehicle(conn, owner_id, vehicle_serial_no):
			print("That person alraedy owns the vehicle.\n")
			continue

		# Are they the primary owner?
		primaryOwner = False
		if not hasGotPrimaryOwner:
			primaryOwner = userInput.getYesNoInput(
				"Are they the primary owner (y) or (n): ")
			hasGotPrimaryOwner = hasGotPrimaryOwner or primaryOwner

		# Do insert
		curs = conn.cursor()
		curs.execute("INSERT INTO owner VALUES "
			"('%s', '%s', '%s')" %
			(owner_id, vehicle_serial_no, 'y' if primaryOwner else 'n'))
		conn.commit()

	# Done
	print("<<< Owners Added >>>\n\n")


# Set up vehicle registration 
def setupVehicleReg(conn):
	try:
		vehicle_serial_no = vehicleRegPart(conn)
		try:
			addOwnersPart(conn, vehicle_serial_no)
		except KeyboardInterrupt:
			print("\n\n<<< Canceled Adding Owners >>>\n")
	except KeyboardInterrupt:
		print("\n\n<<< Canceled Registering Vehicle >>>\n")


# Deals with auto transaction
# Must delete old owner, and add new owner
import cx_Oracle
import datetime
import userInput
import person
import vehicle


# Ensure that a given person exists, or exit
def ensureExists(conn, sin):
	if not person.checkExists(conn, sin):
		shouldRegister = userInput.getYesNoInput(
			"No person with that SIN exists in the database.\n"
			"Do you want to register them? (y) or (n): ")
		if shouldRegister:
			didRegister = person.register(conn, sin)
			if not didRegister:
				return False
		else:
			return False
	return True


# Is a valid vehicle serial number?
def isValidSerialNo(conn, serial):
	# Must not be empty
	if serial == "":
		return "Serial number must not be empty"

	# Serial Must not exist yet
	if not vehicle.checkExists(conn, serial):
		return "That serial number is not registered"

	return True


# Is a given seller a valid seller for a vehicle
# (are they a primary owner)
def isValidSeller(conn, seller, vin):
	# Must not be empty
	if seller == "":
		return "Seller SIN must not be empty"

	# Must be an owner
	if not vehicle.hasOwner(conn, vin, seller):
		return "Seller is not an owner of the vehicle"

	# Must be primary owner
	if not vehicle.hasPrimaryOwner(conn, vin, seller):
		return "Seller is not a primary owner of the vehicle"

	return True


# Get the inputs and perform the transaction
def performTransactionImpl(conn):
	print("Auto Transaction Registration")

	# Get the vehicle to transact
	vin = userInput.getValidatedInput("Serial no of vehicle being sold: ",
		lambda result: isValidSerialNo(conn, result))

	# Get the seller
	seller_sin = userInput.getValidatedInput("Seller SIN: ",
		lambda result: isValidSeller(conn, result, vin))

	# Get the buyers
	buyer_list = []
	while True:
		buyer_sin = userInput.getNonEmptyInput(
			"Enter a buyer SIN" + 
			(" (done if no more buyers)" if buyer_list else "") + 
			": ")

		# Done?
		if buyer_sin == 'done':
			if buyer_list:
				break
			else:
				print("Sale must have at least one buyer")
				continue

		# Ensure that the buyer exists
		if not ensureExists(conn, buyer_sin):
			continue

		# Ensure that they are not an owner
		if vehicle.hasOwner(conn, vin, buyer_sin):
			print("That person already owns the vehicle")
			continue

		# Are they a primary owner
		willPrimary = userInput.getYesNoInput("Will they be a primary owner? (y) / (n): ")

		# Record the buyer
		buyer_list.append((buyer_sin, willPrimary))

	# Date of sale
	date = userInput.getDateInput("Date of sale (yyyy/mm/dd): ")

	# Price
	price = userInput.getNonEmptyInput("Price sold for: ")

	# Get the next txid
	curs = conn.cursor()
	txid = curs.execute("SELECT max(transaction_id)+1 FROM auto_sale").fetchall()[0][0]

	# Add the transaction
	curs.execute(
		"INSERT INTO auto_sale(transaction_id, seller_id, buyer_id, vehicle_id, s_date, price) "
		"VALUES (%d, '%s', '%s', '%s', to_date('%s', 'yyyy/mm/dd'), %s)" %
		(txid, seller_sin, buyer_list[0][0], vin, date, price))

	# Remove all of the current owners
	curs.execute("DELETE FROM owner WHERE vehicle_id = '%s'" % vin)

	# Add the buyers as owners
	for entry in buyer_list:
		curs.execute("INSERT INTO owner VALUES "
			"('%s', '%s', '%s')" % (entry[0], vin, 'y' if entry[1] else 'n'))

	# Finally commit the transaction
	conn.commit()

	print("<<< Transaction Registered >>>\n\n")


# Set up vehicle registration 
def performTransaction(conn):
	try:
		performTransactionImpl(conn)
	except KeyboardInterrupt:
		print("\n\n<<< Canceled Performing Transaction >>>\n")




# Check if a vehicle with a given serial number exists
def checkExists(conn, serial):
	curs = conn.cursor()
	curs.execute("SELECT count(*) FROM vehicle WHERE serial_no = '%s'" % serial)
	return curs.fetchall()[0][0] > 0

# Check if vehicle serial has owner sin
def hasOwner(conn, serial, sin):
	curs = conn.cursor()
	curs.execute(
		"SELECT count(*) FROM owner WHERE owner_id = '%s' AND vehicle_id = '%s'" %
		(sin, serial))
	return curs.fetchall()[0][0] > 0

# Check if vehicle serial has owner sin and is the primary owner
def hasPrimaryOwner(conn, serial, sin):
	curs = conn.cursor()
	curs.execute(
		"SELECT count(*) FROM owner WHERE owner_id = '%s' AND vehicle_id = '%s' AND is_primary_owner = 'y'" %
		(sin, serial))
	return curs.fetchall()[0][0] > 0
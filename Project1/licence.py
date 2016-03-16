
# Check if a licence with a given number exists
def checkExists(conn, number):
	curs = conn.cursor()
	curs.execute("SELECT count(*) FROM drive_licence WHERE licence_no = '%s'" % number)
	return curs.fetchall()[0][0] > 0
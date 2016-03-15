import sys
import cx_Oracle
import datetime
import time

# Gathers information to enter new driver

def setupDriver(logString):
	sin = input("Enter SIN: ")
	DriveClass = input("Enter Class: ")
	# from pymotw.com/2/datetime 
	CurrTime = datetime.date.today()
	# expire date is 5 years from issued date
	expTime = expireDate(datetime.date.today())
	# TODO Add picture to insert into blob
	# Should Licence be generated and not typed in? 
	licenceNo = input("Enter Licence number: ") 
	# TODO check if SIN doesn't exist and ask to add to database
	# TODO check if licence number is already in database 
	# TODO check if licence type+SIN is unique (only one licence per class)
	# TODO add into Database
	
	

# Code tken from: http://stackoverflow.com/questions/15741618/add-one-year-in-current-date-python	
def expireDate(thisDate):
	try:
		return thisDate.replace(year = thisDate.year + 5)
	# To handle feb 29th.
	except:
		return thisDate + (date(thisDate.year + 5, 1, 1,) - date(thisDate.year, 1, 1))
if __name__ == "__main__":
	setupDriver("Test")


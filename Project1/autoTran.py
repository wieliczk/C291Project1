# Deals with auto transaction
# Must delete old owner, and add new owner
import cx_Oracle
import datetime

def autoTrans(logString):
	# Seller and buyer = sin 
	sellerID = input("Seller's SIN: ")
	buyerID = input("Buyer's SIN: ")
	vehID = input("Vehicle Serial Num: ")
	tranDate = datetime.date.today()
	checks = 0
	# Makes sure int input correct
	while checks == 0: 
		try:
			tranPrice = int(input("Price: ")) 
			checks = 1
		except:
			print("Requires Int\n")
	while checks == 1:
		try:
			transID = int(input("Transaction ID: "))
			checks = 2
		except:
			print("Requires Int\n")
# TODO find old owner and remove owner ship
# TODO make buyer new owner
 
def main():
	autoTrans("Test") 

if __name__ == "__main__":
	main()


import sys
import cx_Oracle
import getpass

def connectOracle():
        user = input("Username: ")
        password = getpass.getpass()
        conTry = ''+user+'/' + password + '@gwynne.cs.ualberta.ca:1521/CRS'
        try:
                connection = cx_Oracle.connect(conTry)
                connection.close()
                print("Login Sucessful!\n")
                return 1, conTry
        except:
                print("Incorrect")
                return 0, null

def controlOptions():
        # User chooses which option
        print("(1): New Vehicle Registration \n(2): Auto Transaction \n" \
              "(3): Driver Licence Registration \n(4): Violation Record \n" \
              "(5): Search \n")
        chooses = 0
        while chooses == 0:
                try:
                        chosen = input("Choose a number or 'q' to quit: ")
                        if chosen == "q":
                                break
                        else:
                                chosen = int(chosen)
                        while chosen not in [1,2,3,4,5]:
                                print("Invalid")
                                chosen = input("Choose a number: ")
                                if chosen == "q":
                                        break
                                else:
                                        chosen = int(chosen)
                        chooses = 1
                except:
                        print("Incorrect")
        return chosen

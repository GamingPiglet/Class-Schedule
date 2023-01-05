import os
import sys
import datetime
import pytz
from replit import db

print("Welcome " + os.getenv("REPL_OWNER")) # prints a little welcome message for the user
currenttime = datetime.datetime.now(pytz.timezone("America/Toronto"))
day = currenttime.day % 2

if "Period 4" in db.keys():
	print("Here's today's schedule: \n")
	print("1\t-\t" + db["Period 1"] + "\n" + "2\t-\t" + db["Period 2"] + "\n" + "3\t-\t" + db["Period " + str(4 - day)] + "\n" + "4\t-\t" + db["Period " + str(3 + day)] + "\n")

while True:
	print("What would you like to do?")
	if not "Period 4" in db.keys():
		print("1\t-\tMake Schedule")
		print("2\t-\tEnd Program")
		command = input("Command: ")
		if command == "1":
			print("Please enter your classes in the order you have them today:")
			db["Period 1"] = sys.stdin.readline().strip()
			db["Period 2"] = sys.stdin.readline().strip()
			db["Period " + str(4 - day)] = sys.stdin.readline().strip()
			db["Period " + str(3 + day)] = sys.stdin.readline().strip()
			print("Schedule successfully saved.")
		elif command == "2":
			print("Thank you for using the program.")
			break
		else:
			print("Invalid input, please try again.")
	else:
		print("1\t-\tEdit Schedule")
		print("2\t-\tDelete Schedule")
		print("3\t-\tPrint schedule")
		print("4\t-\tEnd Program")
		command = input("Command: ")
		if command == "1":
			print("Here's your current schedule:\n")
			print("1\t-\t" + db["Period 1"] + "\n" + "2\t-\t" + db["Period 2"] + "\n" + "3\t-\t" + db["Period " + str(4 - day)] + "\n" + "4\t-\t" + db["Period " + str(3 + day)] + "\n")
			edit = input("Please enter the number of the class you want to replace: ")
			if (edit.isnumeric() and 1 <= int(edit) <= 4):
				if edit == "1" or edit == "2":
					db["Period " + edit] = input("Please enter the replacement class: ")
				elif edit == "3":
					db["Period " + str(4 - day)] = input("Please enter the replacement class: ")
				elif edit == "4":
					db["Period " + str(3 + day)] = input("Please enter the replacement class: ")
				print("Class replaced successfully.")
			else:
				print("Invalid input, going back to command menu...")
		elif command == "2":
			confirm = input("Are you sure? (y/n): ")
			if confirm == "y":
				db.clear()
				print("Schedule successfully deleted.")
			else:
				print("Going back...")
		elif command == "3":
			print("Here's today's schedule: \n")
			print("1\t-\t" + db["Period 1"] + "\n" + "2\t-\t" + db["Period 2"] + "\n" + "3\t-\t" + db["Period " + str(4 - day)] + "\n" + "4\t-\t" + db["Period " + str(3 + day)] + "\n")
		elif command == "4":
			print("Thank you for using the program.")
			break
		else:
			print("Invalid input, please try again.")

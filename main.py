import os
import sys
import datetime
import pytz
from replit import db

print("Welcome " + os.getenv("REPL_OWNER")) # prints a little welcome message for the user
currenttime = datetime.datetime.now(pytz.timezone("America/Toronto"))
day = currenttime.day % 2

if (not "Period 3" in db.keys()):
	print("What would you like to do?")
	while True:
		print("1\t-\tMake Schedule")
		print("2\t-\tEnd Program")
		print("Command:", end=" ")
		command = sys.stdin.readline().trim()
		if command == "1":
			print("Please enter your classes in the order you have them today:")
			db["Period 1"] = sys.stdin.readline().trim()
			db["Period 2"] = sys.stdin.readline().trim()
			db["Period " + str(3 + day)] = sys.stdin.readline().trim()
			db["Period " + str(4 - day)] = sys.stdin.readline().trim()
			print("Schedule successfully saved.")
			schedule = db["Period 1"] + "\n" + db["Period 2"] + "\n" + db["Period " + str(3 + day)] + "\n" + db["Period " + str(4 - day)] + "\n"
			break
		elif command == "2":
			print("Thank you for using the program.")
			sys.exit()
		else:
			print("Invalid input, please try again.")
else:
	schedule = "1\t-\t" + db["Period 1"] + "\n" + "2\t-\t" + db["Period 2"] + "\n" + "3\t-\t" + db["Period " + str(3 + day)] + "\n" + "4\t-\t" + db["Period " + str(4 - day)] + "\n"
	print("Here's today's schedule: \n\n" + schedule)

print("What would you like to do?")
while True:
	print("1\t-\tEdit Schedule")
	print("2\t-\tPrint schedule")
	print("3\t-\tEnd Program")
	print("Command:", end=" ")
	command = sys.stdin.readline().trim()
	if command == "1":
		print("Here's your current schedule:")
		print(schedule)
		print("Please enter the number of the class you want to replace:", end=" ")
		edit = sys.stdin.readline().trim()
		print("Please enter the replacement class:", end=" ")
		if edit == "1" or edit == "2":
			db["Period " + edit] = sys.stdin.readline().trim()
			print("Class replaced successfully.")
		elif edit == "3":
			db["Period " + str(3 + day)] = sys.stdin.readline().trim()
			print("Class replaced successfully.")
		elif edit == "4":
			db["Period " + str(4 - day)] = sys.stdin.readline().trim()
			print("Class replaced successfully.")
		else:
			print("Invalid input, going back to command menu...")
	elif command == 2:
		print("Here's today's schedule: \n\n" + schedule)
	elif command == 3:
		print("Thank you for using the program.")
		sys.exit()
	else:
		print("Invalid input, please try again.")

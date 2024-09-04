# for later https://developers.google.com/identity/protocols/oauth2/service-account#python

import os
import sys
import datetime
import pytz
import json
from googleapiclient.discovery import build
from replit import db
from google.oauth2 import service_account

print("Welcome " + os.getenv("REPL_OWNER")) # prints a little welcome message for the user
currenttime = datetime.datetime.now(pytz.timezone("America/Toronto"))
day = currenttime.day % 2
credentials = service_account.Credentials.from_service_account_info(json.loads(os.getenv("API_CREDENTIALS")), scopes=["https://www.googleapis.com/auth/calendar"]) # initialize credentials from credentials secret
client = build('calendar', 'v3', discoveryServiceUrl="https://calendar-json.googleapis.com/$discovery/rest?version=v3", credentials=credentials) # set up google calendar api client to decide what times classes occur. i could just not use the discoveryServiceUrl field but for some reason it can't find the api without it
daysoff = client.events().list(calendarId="c_d3boa08h5mvnj1c7bb218hj6ao@group.calendar.google.com", maxResults=1,  singleEvents=True, timeMin=datetime.datetime.utcnow().isoformat() + "Z").execute()["items"]
dayoffbegin = datetime.datetime.combine(datetime.datetime.strptime(daysoff[0]["start"]["date"], "%Y-%m-%d"), datetime.datetime.min.time())
dayoffend = datetime.datetime.combine(datetime.datetime.strptime(daysoff[0]["start"]["date"], "%Y-%m-%d"), datetime.datetime.max.time())
if "elementary" in daysoff[0]["summary"] and not "secondary" in daysoff[0]["summary"]:
	dayoffbegin = datetime.datetime.combine(datetime.datetime.strptime(daysoff[1]["start"]["date"], "%Y-%m-%d"), datetime.datetime.min.time())
	dayoffend = datetime.datetime.combine(datetime.datetime.strptime(daysoff[1]["start"]["date"], "%Y-%m-%d"), datetime.datetime.max.time())

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
			if currenttime.month == 9:
				firstday = client.events().list(calendarId="c_d3boa08h5mvnj1c7bb218hj6ao@group.calendar.google.com", q="first day of school", singleEvents=True, timeMin=str(currenttime.year)+ "-01-01T00:00:00.000000Z").execute()["items"]
				comparefirstday = datetime.datetime.combine(datetime.datetime.strptime(firstday[0]["start"]["date"], "%Y-%m-%d"), datetime.datetime.min.time())
				if currenttime >= comparefirstday:
					print("Here's today's schedule: \n")
					print("1\t-\t" + db["Period 1"] + "\n" + "2\t-\t" + db["Period 2"] + "\n" + "3\t-\t" + db["Period " + str(4 - day)] + "\n" + "4\t-\t" + db["Period " + str(3 + day)] + "\n")
				else:
					print("No school today.")
			elif currenttime.month == 7 or currenttime.month == 8:
				print("No school today.")
			elif len(daysoff) > 0 and currenttime >= dayoffbegin and currenttime <= dayoffend:
				if  daysoff[0]["summary"].lower():
					print("Here's today's schedule: \n")
					print("1\t-\t" + db["Period 1"] + "\n" + "2\t-\t" + db["Period 2"] + "\n" + "3\t-\t" + db["Period " + str(4 - day)] + "\n" + "4\t-\t" + db["Period " + str(3 + day)] + "\n")
				else :
					print("No school.")
			else:
				print("Here's today's schedule: \n")
				print("1\t-\t" + db["Period 1"] + "\n" + "2\t-\t" + db["Period 2"] + "\n" + "3\t-\t" + db["Period " + str(4 - day)] + "\n" + "4\t-\t" + db["Period " + str(3 + day)] + "\n")
		elif command == "4":
			print("Thank you for using the program.")
			break
		else:
			print("Invalid input, please try again.")

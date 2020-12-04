import datetime
import pyttsx3
import time
import sqlite3

# Connection to sqlite database
conn = sqlite3.connect("reminders.db")
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS reminders
			 (date text, reminderFor text)''')

# Initializing text-to-speech engine
engine = pyttsx3.init()

addOrNot = input("Do you want to add a reminder? ")
if addOrNot.lower() == "yes":
	timeForReminder = input("When do you want the reminder to be? ")
	reminderFor = input("What is the reminder for? ")

	timeForReminder = timeForReminder.split("/")
	timeForReminder = [int(i) for i in timeForReminder]
	timeForReminder = str(datetime.datetime(timeForReminder[2], timeForReminder[0], timeForReminder[1]).date())

	# Need to make secure and not use f string
	c.execute("INSERT INTO reminders VALUES (?, ?)", (timeForReminder, reminderFor))
	conn.commit()

	engine.say("Reminder added")
	engine.runAndWait()
	print("Reminder added")

	conn.close()

elif addOrNot.lower() == "no":
	today = str(datetime.datetime.now().date())

	c.execute("SELECT * FROM reminders")
	reminders = c.fetchall()

	for reminder in reminders:
		time = reminder[0]
		reminderFor = reminder[1]
		time = time.split("-")
		time = datetime.datetime(int(time[0]), int(time[1]), int(time[2]))

		if str(time.date()) == today:
			print(f"Hey yo you have a reminder for {reminderFor}")
			engine.say(f"Hey yo you have a reminder for {reminderFor}")
			engine.runAndWait()

	c.execute('''DELETE FROM reminders WHERE ?''', )

	conn.close()

else:
	engine.say("Please say yes or no.")
	engine.runAndWait()
	print("Please say yes or no.")

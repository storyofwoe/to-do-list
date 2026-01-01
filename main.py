#py -m pip install <package> in cmd terminal
import inflect
import datetime
p = inflect.engine()

reminders = []
dates = []

while True:
    remindLen = len(reminders)
    isNotEmpty = bool(remindLen)
    print(f"There {p.plural("is", remindLen)} currently {remindLen} {p.plural("reminder",remindLen)} in your list.")

    ext = ""
    if isNotEmpty:
        ext = ", 'EDIT' followed by its ID to edit a reminder, or 'DELETE' followed by its ID to delete a reminder"
    print("Type 'CREATE' to create one" + ext + ".")

    if isNotEmpty:
        print("ID  | Date                | Reminder")
        print("----+---------------------+---------")
        for x in range(remindLen):
            print(f"{str(x+1).ljust(3)} | {str(dates[x]).ljust(19)} | {reminders[x]}") #consider using textwrap package to wrap text if it's too long

    print()

    cmd = input().lower()
    if cmd == "create":
        print("Please enter your reminder.")
        print()
        entry = input()
        print("Please enter a date and time, if applicable.")
        inputYear = input("Year: ")
        inputMonth = input("Month: ")
        inputDay = input("Day: ")
        inputHour = input("Hour: ")
        inputMinute = input("Minute: ")

        test = []
        try:
            year = int(inputYear)
            month = int(inputMonth)
            day = int(inputDay)
            hour = int(inputHour)
            minute = int(inputMinute)
        except:
            dates.append("") #need to individually test year, month, etc. and only put in "dates" whichever ones were given values
        else:
            entryDate = datetime.datetime(year, month, day, hour, minute)
            dates.append(entryDate)
        
        reminders.append(entry)        
        print("Reminder successfully added.")
        print()
    elif "edit" in cmd:
        id = [int(s) for s in cmd.split() if s.isdigit()][0] #retrieves the id from the input
        print("Please enter your new reminder.")
        print()
        reminders[id-1] = input()
    elif "delete" in cmd:
        id = [int(s) for s in cmd.split() if s.isdigit()][0]
        reminders.pop(id-1)
        print("Reminder successfully deleted.")
        print()
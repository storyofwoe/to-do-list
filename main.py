#py -m pip install <package> in cmd terminal
import inflect #manual install required
import datetime
p = inflect.engine()
import json
import sys

try:
    with open("reminders.json", "r") as file:
        remindersDict = json.load(file)
except:
    remindersDict = {}

reminders = list(remindersDict.keys())
strDates = list(remindersDict.values())
#dates = [0 for x in strDates]

def reminderDateToString():
    print("Please enter a date and time, if applicable.")
    year = input("Year: ")
    month = input("Month: ")
    day = input("Day: ")
    hour = input("Hour: ")
    minute = input("Minute: ")
    try: #records input as number if non-empty
        intMinute = int(minute)
    except:
        intMinute = None
    finally:
        try:
            intHour = int(hour)
        except:
            intHour = None
        finally:
            try:
                intDay = int(day)
            except:
                intDay = None
            finally:
                try:
                    intMonth = int(month)
                except:
                    intMonth = None
                finally:
                    try:
                        intYear = int(year)
                    except:
                        intYear = None

    #try and figure out how to only include given date/time in final list, using something that's a bit cleaner than below
    parts = []
    if intYear and intMonth:
        if intDay:
            dt = datetime.date(intYear, intMonth, intDay)
            parts.append(dt.strftime("%d %B %Y"))
        else:
            dt = datetime.date(intYear, intMonth, 1)
            parts.append(dt.strftime("%B %Y"))
        if intHour is not None and intMinute is not None:
            dt = datetime.time(intHour, intMinute)
            parts.append(dt.strftime("%H:%M"))
    dateStr = " at ".join(x for x in parts if x)
    return dateStr
    #dates.append(dateStr)   

while True:
    remindLen = len(reminders)
    isNotEmpty = bool(remindLen)
    today = datetime.datetime.now()

    print(f"There {p.plural("is", remindLen)} currently {remindLen} {p.plural("reminder",remindLen)} in your list.")

    ext = ""
    if isNotEmpty:
        ext = ", 'EDIT' followed by its ID to edit a reminder, 'DELETE' followed by its ID to delete a reminder"
    print("Type 'CREATE' to create one" + ext + ", or EXIT to close.")

    if isNotEmpty:
        print("ID  | Date                      | Reminder")
        print("----+---------------------------+---------")
        for x in range(remindLen):
            print(f"{str(x+1).ljust(3)} | {str(strDates[x]).ljust(25)} | {reminders[x]}") #consider using textwrap package to wrap text if it's too long

    print()

    cmd = input().lower()
    if cmd == "create":
        print("Please enter your reminder.")
        entry = input()    

        strDates.append(reminderDateToString())

        # inputtedDates = dict(year = intYear, month = intMonth, day = intDay, hour = intHour, minute = intMinute)
        # values = list(inputtedDates.values())
        # dateParts = [x for x in values if x is not None] #forms list of values that aren't None
        # print(dateParts) 
        
        reminders.append(entry)        
        print("Reminder successfully added.")
        print()

    elif "exit" in cmd:
        remindersDict = dict(zip(reminders, strDates))
        with open("reminders.json", "w") as file:
            json.dump(remindersDict, file)
        sys.exit()

    try:
        cmdSplit = [int(s) for s in cmd.split() if s.isdigit()]
    except:
        pass
    else:
        if len(cmdSplit) == 1:
            remindId = cmdSplit[0]
            if remindId <= remindLen:
                if "edit" in cmd:
                    print("Type 'CONTENT' to edit the content of your reminder, 'DATE' to edit the date of the reminder, or 'BACK' to go back.")
                    editCmd = input().lower()
                    if "back" in editCmd:
                        pass
                    elif "content" in editCmd:
                        print("Please enter your new reminder.")
                        reminders[remindId-1] = input()
                        print("Reminder successfully edited.")
                        print()
                    elif "date" in editCmd:
                        strDates[remindId-1] = reminderDateToString()
                    
                elif "delete" in cmd:
                    reminders.pop(remindId-1)
                    print("Reminder successfully deleted.")
                    print()
#py -m pip install <package> in cmd terminal
import inflect
import datetime
p = inflect.engine()

reminders = ["test"]
dates = [""]

while True:
    remindLen = len(reminders)
    isNotEmpty = bool(remindLen)
    today = datetime.datetime.now()

    print(f"There {p.plural("is", remindLen)} currently {remindLen} {p.plural("reminder",remindLen)} in your list.")

    ext = ""
    if isNotEmpty:
        ext = ", 'EDIT' followed by its ID to edit a reminder, or 'DELETE' followed by its ID to delete a reminder"
    print("Type 'CREATE' to create one" + ext + ".")

    if isNotEmpty:
        print("ID  | Date                      | Reminder")
        print("----+---------------------------+---------")
        for x in range(remindLen):
            print(f"{str(x+1).ljust(3)} | {str(dates[x]).ljust(25)} | {reminders[x]}") #consider using textwrap package to wrap text if it's too long

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

        try: #records input as number if non-empty
            intMinute = int(inputMinute)
        except:
            intMinute = None
        finally:
            try:
                intHour = int(inputHour)
            except:
                intHour = None
            finally:
                try:
                    intDay = int(inputDay)
                except:
                    intDay = None
                finally:
                    try:
                        intMonth = int(inputMonth)
                    except:
                        intMonth = None
                    finally:
                        try:
                            intYear = int(inputYear)
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
            dt = datetime.datetime(1, 1, 1, intHour, intMinute)
            parts.append(dt.strftime("%H:%M"))
        dateStr = " at ".join(x for x in parts if x)
        dates.append(dateStr)

        # inputtedDates = dict(year = intYear, month = intMonth, day = intDay, hour = intHour, minute = intMinute)
        # values = list(inputtedDates.values())
        # dateParts = [x for x in values if x is not None] #forms list of values that aren't None
        # print(dateParts) 
        
        reminders.append(entry)        
        print("Reminder successfully added.")
        print()

    elif "edit" in cmd:
        try:
            cmdSplit = [int(s) for s in cmd.split() if s.isdigit()]            
        except:
            pass
        else:
            if len(cmdSplit) == 1:
                remindId = cmdSplit[0] #retrieves the id from the input, only if 1 number was given
                if remindId <= remindLen: #makes sure id given is in the bounds of the length of the reminder list
                    print("Please enter your new reminder.")
                    print()
                    reminders[remindId-1] = input()

    elif "delete" in cmd:
        try:
            cmdSplit = [int(s) for s in cmd.split() if s.isdigit()]
        except:
            pass
        else:
            if len(cmdSplit) == 1:
                remindId = cmdSplit[0]
                reminders.pop(remindId-1)
                print("Reminder successfully deleted.")
                print()
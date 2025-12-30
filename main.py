#py -m pip install <package> in cmd terminal
import inflect
p = inflect.engine()

reminders = ["test", "test2"]

while True:
    remindLen = len(reminders)
    print(f"There {p.plural("is", remindLen)} currently {remindLen} {p.plural("reminder",remindLen)} in your list.")

    ext = ""
    if remindLen > 0:
        ext = ", or 'EDIT' followed by its ID to edit a reminder"
    print("Type 'CREATE' to create one" + ext + ".")
    print()

    if remindLen > 0:
        print("ID  |  Reminder")
        print("----+----------")
        for x in range(remindLen):
            print(f"{str(x+1).ljust(3)} | {reminders[x]}") #consider using textwrap package to wrap text if it's too long

    print()

    cmd = input().lower()
    if cmd == "create":
        print("Please enter your reminder.")
        print()
        entry = input()
        reminders.append(entry)
    elif "edit" in cmd:
        id = [int(s) for s in cmd.split() if s.isdigit()][0]
        print("Please enter your new reminder.")
        print()
        reminders[id-1] = input()
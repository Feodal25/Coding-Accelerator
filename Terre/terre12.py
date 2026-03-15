import sys
arguments = sys.argv[1:]

if len(arguments) != 1:
    sys.exit("arguments number incorrect")

time = arguments[0]

if len(time) != 7:
    sys.exit("argument must be the time in format 12h")

if not time[:2].isdigit() or not time[3:5].isdigit() or time[2] != ":" or time[5:7] not in ["AM", "PM", "am", "pm"]:
    sys.exit("argument must be time in format 12h")

print(time)
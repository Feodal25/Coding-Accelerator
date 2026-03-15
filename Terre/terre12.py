import sys
arguments = sys.argv[1:]

if len(arguments) != 1:
    sys.exit("arguments number incorrect")

time = arguments[0]

if len(time) != 7:
    sys.exit("argument must be the time in format 12h")

if not time[:2].isdigit() or not time[3:5].isdigit() or time[2] != ":" or time[5:7] not in ["AM", "PM", "am", "pm"]:
    sys.exit("argument must be time in format 12h")

hours = ""
minutes = ""
period = ""

for char in time:
    if char == ":":
        break
    else:
        hours += char

for char in time[3:5]:
    minutes += char

for char in time[5:7]:
    period += char

print(hours)
print(minutes)
print(period)

hours = int(hours)
minutes = int(minutes)

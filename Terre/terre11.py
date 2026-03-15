import sys
arguments = sys.argv[1:]

if len(arguments) != 1:
    sys.exit("arguments number incorrect")

time = arguments[0]

if len(time) != 5:
    sys.exit("argument must be the time in format 24h")

if not time[:2].isdigit() or not time[3:].isdigit() or time[2] != ":":
    sys.exit("argument must be time in format 24h")

hours = int(time[:time.find(":")])
minutes = int(time[time.find(":") + 1:])

period = ""

if hours >= 12:
    period = "PM"
else:
    period = "AM"

if hours > 12:
    hours -= 12

if hours == 0:
    hours = "00"

print(f"{hours}:{minutes}{period}")
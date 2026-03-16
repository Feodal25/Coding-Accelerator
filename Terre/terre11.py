import sys
arguments = sys.argv[1:]

if len(arguments) != 1:
    sys.exit("arguments number incorrect")

time = arguments[0]

if len(time) != 5:
    sys.exit("argument must be the time in format 24h")

if not time[:2].isdigit() or not time[3:].isdigit() or time[2] != ":":
    sys.exit("argument must be time in format 24h")

hours = ""
minutes = ""

for char in time:
    if char == ":":
        break
    else:
        hours += char

for char in time[3:]:
    minutes += char

hours = int(hours)
minutes = int(minutes)
period = ""

if hours >= 12:
    period = "PM"
else:
    period = "AM"

if hours > 12:
    hours -= 12

if hours < 10:
    hours = f"0{hours}"

print(f"{hours}:{minutes}{period}")
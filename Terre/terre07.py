import sys
arguments = sys.argv[1:]

if len(arguments) != 1:
    sys.exit("écris une chaîne de caractères")

if arguments[0].isdigit():
    sys.exit("écris une chaîne de caractères")

string = arguments[0]
count = 0

for character in string:
    count += 1

print(count)
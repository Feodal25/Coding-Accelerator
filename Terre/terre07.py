import sys
arguments = sys.argv[1:]

if len(arguments) != 1:
    sys.exit("écris une chaîne de caractères")

entry = arguments[0]

if entry.isdigit():
    sys.exit("écris une chaîne de caractères")

entry_length = 0

for i in entry:
    entry_length += 1

print(entry_length)
import sys
arguments = sys.argv[1:]

if len(arguments) != 1:
    print("écris une chaîne de caractères")
    sys.exit()

entry = arguments[0]
reverse_entry = ""

for i in range(len(entry) -1, -1, -1):
    reverse_entry += entry[i]

print(reverse_entry)
import sys
arguments = sys.argv[1:]

if len(arguments) != 1:
    sys.exit("écris une chaîne de caractères")

argument = arguments[0]

if argument.isdigit():
    sys.exit("écris une chaîne de caractères")

count = 0

for caracters in argument:
    count += 1

print(count)
import sys
arguments = sys.argv[1:]

if len(arguments) != 1:
    sys.exit("arguments number incorrect")

if not arguments[0].isdigit():
    sys.exit("argument must be a positif number")

radicand = int(arguments[0])
impairs = 1
count = 0

while radicand > 0:
    radicand = radicand - impairs
    impairs += 2
    count += 1

if radicand != 0:                                               # Pour arrondir vers le bas lorsque not carré parfait
    print(count -1)
else:
    print(count)
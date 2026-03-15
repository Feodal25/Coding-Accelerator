import sys
arguments = sys.argv[1:]

if len(arguments) != 1:
    sys.exit("arguments number incorrect")

if not arguments[0].isdigit():
    sys.exit("argument must be a positif number")

number = int(arguments[0])
divisor = 2

while number > divisor:
    if (number / divisor) % 1 == 0:
        print(f"Non, {number} n'est pas un nombre premier.")
        break
        
    else:
        divisor += 1
else:
    print(f"Oui, {number} est un nombre premier.")
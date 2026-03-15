import sys
arguments = sys.argv[1:]

if len(arguments) != 1:
    sys.exit("arguments number incorrect")

if not arguments[0].isdigit():
    sys.exit("argument must be a positif number")

number = int(arguments[0])

if number <= 1:                                                     # J'exclue 0 et 1 de mes scénarios car chiant pour formule après
    print(f"Non, {number} n'est pas un nombre premier.")
    sys.exit()

if number == 2:
    print(f"Oui, {number} est un nombre premier")                   # J'exclue également 2 de mes scénarios car divisor = 2
    sys.exit()

divisor = 2

while number > divisor:
    if (number / divisor) % 1 == 0:
        print(f"Non, {number} n'est pas un nombre premier.")
        break
        
    else:
        divisor += 1
else:
    print(f"Oui, {number} est un nombre premier.")
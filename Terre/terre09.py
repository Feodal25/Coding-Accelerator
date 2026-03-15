import sys
arguments = sys.argv[1:]

if len(arguments) != 1:
    sys.exit("arguments number incorrect")

if not arguments[0].isdigit():
    sys.exit("argument must be a positif number")

radicand = int(arguments[0])
x = 10
x_suivant = radicand / 2

while abs(x_suivant - x) > 0.0001:
    x = x_suivant
    x_suivant = (x + radicand/x) / 2

result = x_suivant

print(f"{result:.4f}")
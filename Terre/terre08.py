import sys
arguments = sys.argv[1:]

if len(arguments) != 2:
    sys.exit("incorrect arguments number")

if not all(argument.isdigit() for argument in arguments):
    sys.exit("arguments must be positive numbers")

base = int(arguments[0])
exponent = int(arguments[1])

if exponent == 0:
    sys.exit("exponent can't be 0")

result = 1

for i in range(exponent):
    result = result * base

print(result)
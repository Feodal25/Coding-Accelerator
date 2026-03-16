import sys
arguments = sys.argv[1:]

if len(arguments) != 3:
    sys.exit("3 arguments needed")

if not all(argument.isdigit() for argument in arguments):
    sys.exit("arguments must be positive whole numbers")

numbers = [int(n) for n in arguments]

for n in numbers:
    if min(numbers) < n < max(numbers):
        print(n)
        break
else:
    print("erreur.")
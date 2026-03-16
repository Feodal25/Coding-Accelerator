import sys
arguments = sys.argv[1:]

if not all(argument.isdigit() for argument in arguments):
    sys.exit("arguments must be positive whole numbers")

numbers = [int(n) for n in arguments]

if numbers[0] > numbers[1]:
    print("Pas triée!")
    sys.exit()

for i in range(len(numbers) - 1):
    if numbers[i] > numbers[i+1]:
        print("Pas triée !")
        break
else:
        print("Triée !")
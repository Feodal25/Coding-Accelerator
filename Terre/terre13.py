import sys
arguments = sys.argv[1:]

if len(arguments) != 3:
    sys.exit("3 arguments needed")

if not all(argument.isdigit() for argument in arguments):
    sys.exit("arguments must be positive whole numbers")

first_number = arguments[0]
second_number = arguments[1]
third_number = arguments[2]


if third_number > first_number > second_number or second_number > first_number > third_number:
    print(first_number)
elif third_number > second_number > first_number or first_number > second_number > third_number:
    print(second_number)
elif first_number > third_number > second_number or second_number > third_number > first_number:
    print(third_number)
else:
    print("erreur.")
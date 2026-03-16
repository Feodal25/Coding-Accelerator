import sys
arguments = sys.argv[1:]

if len(arguments) != 3:
    sys.exit("3 arguments needed")

if not all(argument.isdigit() for argument in arguments):
    sys.exit("arguments must be positive whole numbers")

first_number = arguments[0]
second_number = arguments[1]
third_number = arguments[2]


if first_number > second_number and first_number < third_number or first_number > third_number and first_number < second_number:
    print(first_number)
elif second_number > first_number and second_number < third_number or second_number > third_number and second_number < first_number:
    print(second_number)
elif third_number > second_number and third_number < first_number or third_number > first_number and third_number < second_number:
    print(third_number)
else:
    print("erreur.")
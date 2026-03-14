import sys
arguments = sys.argv[1:]

if len(arguments) != 1 :
    print("Tu ne me la metteras pas à l'envers")
    sys.exit()


if not arguments[0].removeprefix("-").isdigit():
    print("Tu ne me la metteras pas à l'envers")
    sys.exit()

entry_number = int(arguments[0])

if entry_number % 2 == 0:
    print("pair")
else:
    print("impair")
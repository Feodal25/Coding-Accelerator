import sys

def message_erreur():
    print("erreur.")
    sys.exit()

args = sys.argv[1:]

if len(args) != 2:
    message_erreur()

dividend = args[0]
divisor = args[1]

try:
    dividend = int(dividend)
    divisor = int(divisor)

    if (dividend < divisor):
        message_erreur()
    else:
        result = dividend // divisor
        reminder = dividend % divisor
        print(f"résultat : {result}")
        print(f"reste : {reminder}")
except (ValueError, ZeroDivisionError):
    message_erreur()
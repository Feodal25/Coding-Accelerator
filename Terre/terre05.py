import sys
arguments = sys.argv[1:]

if len(arguments) != 2:
    print("arguments number incorrect")
    sys.exit()

if not all(argument.isdigit() for argument in arguments):
    print("Arguments are not positive whole numbers")
    sys.exit()

dividend = int(arguments[0])
divisor = int(arguments[1])

if divisor == 0:
    print("Divisor can't be equal to 0")
    sys.exit()

if dividend < divisor:
    print("Dividend must be higher than divisor")
    sys.exit()

result = dividend / divisor
remainder = dividend % divisor
rounded_result = ""

for i in str(result):
    if i == ".":
        break
    else:
        rounded_result += i

print(f"résultat : {rounded_result}")
print(f"reste : {remainder}")
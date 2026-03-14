import sys
arguments = sys.argv[1:]

if len(arguments) != 1 or len(arguments[0]) != 1:
	print("argument number or size incorrect")
	sys.exit()

argument = arguments[0]
first_letter = 97
last_letter = 122

if ord(argument) < first_letter or ord(argument) > last_letter:
	print("argument has to be a lowercase letter")
	sys.exit()

starting_letter = ord(argument)
result = ""

for i in range(starting_letter, last_letter + 1):
	result = result + chr(i)
	
print(result)
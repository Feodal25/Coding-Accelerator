import sys
arguments = sys.argv[1:]

if len(arguments) != 1:
	print("argument number incorrect")
	sys.exit()

if len(arguments[0]) != 1:
	print("argument size incorrect")
	sys.exit()

first_letter = 97
last_letter = 122

if ord(arguments[0]) < first_letter or ord(arguments[0]) > last_letter:
	print("argument has to be a lowercase letter")
	sys.exit()

starting_letter = ord(arguments[0])
result = ""

for i in range(starting_letter, last_letter + 1):
	result = result + chr(i)
	
print(result)
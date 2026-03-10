import sys
args = sys.argv[1:]
arg1 = ""
alphabet_from_arg1 = ""
a_ascii = 97
z_ascii = 123

arg1 = arg1 + args[0]
arg1_ascii = ord(arg1)

if len(args) != 1 or len(arg1) != 1 or ord(arg1) < a_ascii or ord(arg1) > z_ascii:
    print("wrong entry... You need to give me one letter of the alphabet in lowercap")
else:
    for i in range(arg1_ascii, z_ascii):
        alphabet_from_arg1 = alphabet_from_arg1 + chr(i)
    print(alphabet_from_arg1)
    
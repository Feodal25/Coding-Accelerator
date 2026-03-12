import sys
args = sys.argv[1:]
def message_erreur():
    print("wrong entry... You need to give me one letter of the alphabet in lowercap")
    sys.exit()

if len(args) != 1:
    message_erreur()

code_first_letter = 97
code_last_letter = 123

if len(args[0]) != 1 or ord(args[0]) < code_first_letter or ord(args[0]) > code_last_letter:
    message_erreur()

alphabet = ""
code_begin_letter = ord(args[0])

for i in range(code_begin_letter, code_last_letter):
    alphabet = alphabet + chr(i)
print(alphabet)
import sys

def message_erreur():
    print("erreur.")
    sys.exit()
def est_valide(arg):
    return arg.isdecimal() or (arg[0] == "-" and arg[1:].isdecimal())

args = sys.argv[1:]

if len(args) != 2:
    message_erreur()

arg1 = args[0]
arg2 = args[1]

if (not est_valide(arg1) or not est_valide(arg2)):
    message_erreur()

arg1 = int(arg1)
arg2 = int(arg2)

if (arg1 < arg2) or (arg2 == 0):
    message_erreur()
else:
    résultat = arg1 // arg2
    reste = arg1 % arg2
    print(f"résultat : {résultat}")
    print(f"reste : {reste}")
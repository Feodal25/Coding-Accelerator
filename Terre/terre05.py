arg1 = 11
arg2 = 4

résultat = arg1 / arg2
résultat = int(résultat)
print(f"résultat : {résultat}")

reste = arg1 % arg2
print(f"reste : {reste}")


#--------------
import sys
args = sys.argv[1:]
if len(args) != 2:
    print("erreur.")
    sys.exit()

arg1 = args[0]
arg2 = args[1]

if (arg1.isdecimal()) or (arg1[0] == "-" and arg1[1:].isdecimal()):

    arg1 = int(arg1)
    arg2 = int(arg2)
    résultat = arg1 / arg2
    reste = arg1 % arg2

    print(f"résultat : {résultat}")
    print(f"reste : {reste}")
else:
    print("erreur.")
import sys
args = sys.argv[1:]
if len(args) != 2:
    print("erreur.")
    sys.exit()

arg1 = args[0]
arg2 = args[1]

if (arg1.isdecimal() and arg2.isdecimal() and (arg1 >= arg2)) or ((arg1[0] == "-" and arg1[1:].isdecimal()) and (arg2[0] == "-" and arg2[1:].isdecimal()) and (arg1 >= arg2)):

    arg1 = int(arg1)
    arg2 = int(arg2)
    résultat = arg1 // arg2                                 # "//" = division entière, retourne toujours un int (arrondi vers le bas)
    résultat = int(résultat)
    reste = arg1 % arg2

    print(f"résultat : {résultat}")
    print(f"reste : {reste}")
else:
    print("erreur.")
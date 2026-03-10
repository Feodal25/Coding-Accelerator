import sys
args = sys.argv[1:]
arg1 = args[0]

if (len(args) == 1 and arg1.isdecimal()) or (arg1[0] == "-" and arg1[1:].isdecimal()):
    print("super on continue")
else:
    print("Tu ne me la mettras pas à l'envers")
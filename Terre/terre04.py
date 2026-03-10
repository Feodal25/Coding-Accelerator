import sys
args = sys.argv[1:]
if len(args) != 1:
    print("Tu ne me la mettras pas à l'envers")
    sys.exit()

arg1 = args[0]

if (arg1.isdecimal()) or (arg1[0] == "-" and arg1[1:].isdecimal()):
    arg1 = int(arg1)
    if arg1 % 2 == 0:
        print("pair")
    else:
        print("impair")
else:
    print("Tu ne me la mettras pas à l'envers")
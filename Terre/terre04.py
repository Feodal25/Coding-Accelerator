import sys
args = sys.argv[1:]
def message_erreur():
    print("Tu ne me la mettras pas à l'envers")
    sys.exit()

if len(args) != 1:
    message_erreur()

arg = args[0].removeprefix("-")

if not arg.isdecimal():
    message_erreur()

int_arg = int(arg)

if int_arg % 2 == 0:
    print("pair")
else:
    print("impair")
import sys
args = sys.argv[1:]
def message_erreur():
    print("Tu ne me la mettras pas à l'envers")
    sys.exit()

if len(args) != 1:
    message_erreur()

try:
    if int(args[0]) % 2 == 0:
        print("pair")
    else:
        print("impair")
except ValueError:
    message_erreur()
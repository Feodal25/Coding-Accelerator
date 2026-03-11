import sys
args = sys.argv[1:]

if len(args) == 0:                                  # pour éviter que si pas d'argument le programme crash
    print("écris quelque chose tu veux")
    sys.exit()

str_args = " ".join(args)
print(str_args[::-1])
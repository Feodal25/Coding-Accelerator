import sys
args = sys.argv[1:]
str_args = ""
count = 0

if len(args) == 0:                                  # pour éviter que si pas d'argument le programme crash
    print("écris quelque chose tu veux")
    sys.exit()

for i in args:                                      # on crée un boucle pour mettre chaque élément de la liste args dans la string str_args
    str_args = str_args + args[count] + " "
    count = count + 1

str_args = str_args[:-1]                            # pour enlever le dernier " " de la boucle
print(str_args[::-1])


first_letter = 97
current_letter = chr(first_letter)
count = 0

while count < 26:
    print(current_letter, end='')
    first_letter += 1
    count += 1
    current_letter = chr(first_letter)

print()

#---------
# Deuxième version : en utilisant une boucle for au lieu de while

alphabet = ""

for i in range(97, 123): 
    alphabet = alphabet + chr(i)

print(alphabet)

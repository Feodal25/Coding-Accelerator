# print("Oui le programme fonctionne !")
#mybirthday = '7/11/2001'
#print("Your birthday is :",mybirthday)

#--------------------------------------------------

# numbers = []
# strings = []
# names = ["John", "Eric", "Jessica"]

# numbers.append(1)
# numbers.append(2)
# numbers.append(3)

# strings.append('hello')
# strings.append('world')

# second_name = names[1]

# # this code should write out the filled arrays and the second name in the names list (Eric).
# print(numbers)
# print(strings)
# print("The second name on the names list is %s" % second_name)


#--------------------------------------------------

# TEST 1 EXERCICE 00

#alphabet = []
#alphabet.append('a')
#alphabet.append('b')
#alphabet.append('c')
#alphabet.append('d')
#alphabet.append('e')
#alphabet.append('f')
#alphabet.append('g')
#alphabet.append('h')
#alphabet.append('i')
#alphabet.append('j')
#alphabet.append('k')
#alphabet.append('l')
#alphabet.append('m')
#alphabet.append('n')
#alphabet.append('o')
#alphabet.append('p')
#alphabet.append('q')
#alphabet.append('r')
#alphabet.append('s')
#alphabet.append('t')
#alphabet.append('u')
#alphabet.append('v')
#alphabet.append('w')
#alphabet.append('x')
#alphabet.append('y')
#alphabet.append('z')

#print(alphabet)

#--------------------------------------------------

#number = 1 + 2 * 3 / 4.0
#modulode11 = 11 % 3
#squared = 7 ** 2
#cubed = 7 ** 2
#helloworld = "hello" + " " + "world"
#lotsofbasile = "basile " * 9
#even_numbers = [2,4,6,8]
#odd_numbers = [1,3,5,7,9]
#all_numbers = odd_numbers + even_numbers
#all_numbers_in_order = sorted(all_numbers, reverse=False)

#print(number)
#print("J'adore le modulo. Et pour le prouver, voici le modulo de 11 :",modulode11)
#print("Je me demande si squared et cubed c'est la même chose en anglais. Ducoup on teste. Voici 7 au caréé :",squared,cubed)
#print(helloworld)
#print("9 Japrisot = ",lotsofbasile)
#print(all_numbers)
#print(all_numbers_in_order)

# Exercice final :

#x = "salut"
#y = "oui"

#x_list = [x] * 10
#y_list = [y] * 10
#big_list = [x] * 10 + [y] * 10


#print(x_list)
#print(y_list)
#print("x_list contains %d objects" % len(x_list))
#print("y_list contains %d objects" % len(y_list))
#print("big_list contains %d objects" % len(big_list))
#print(len(big_list))
#print(len(x))

#--------------------------------------------

#name = "Milla"
#age = 13
#mylist = [1,2,3]
#myfloat = 23.456


#print("Bonjour %s, tu as %d:)" % (name,age))
#print("A list: %s" % mylist)
#print("%.2f" % myfloat)
#print("%x" % age)
#print("%f" % myfloat)



# Exercice final :


# data = ("John", "Doe", 53.44)
# format_string = "Hello"

# print("%s %s %s. Your current balance is $%.2f." % (format_string, data[0], data[1], data[2]))

#----------------

# Variante de learnpython.org mais d'après basile c'est moins bien
# data = ("John", "Doe", 53.44)
# format_string =  "Your current balance is $%s. Hello %s %s."

# print(format_string % data)

#---------------------

# astring = "Basile c'est vraiment un tigre du bengal"

# print(astring.upper())
# print(astring.lower())

# astring = "Hello world!"
# afewwords = astring.split(" ")

# print(afewwords)
# print(len(afewwords))
# print(len(astring))

# s = "Hey there! what shou"

# print(len(s))

#-------------------------------------------

# change this code
# change this code
# number = 16
# second_number = 0
# first_array = [1,2,3]
# second_array = [1,2]

# if number > 15:
#     print("1")

# if first_array:
#     print("2")

# if len(second_array) == 2:
#     print("3")

# if len(first_array) + len(second_array) == 5:
#     print("4")

# if first_array and first_array[0] == 1:
#     print("5")

# if not second_number:
#     print("6")

#--------------------------------------------------

# Exercice Loops learnpython.org


# numbers = [
#     951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
#     615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
#     386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
#     399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
#     815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
#     958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
#     743, 527
# ]

# # your code goes here
# for number in numbers:
#     if number == 237:
#         break
#     if number % 2==1:
#         continue
#     print(number)

#     ---------------------------------------------


# Exercice Alphabet  Ca maaarche

all_letters = "abcdefghijklmnopqrstuvwxyz"
alphabet = ""

for i in range(len(all_letters)):
    alphabet = alphabet + all_letters[i]

print(alphabet)


#-----------------------

# On test avec ASCII mtn
#print(ASCII(1))
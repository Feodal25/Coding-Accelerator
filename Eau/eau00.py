def add_leading_zeros(number):
    chars = str(number)
    while len(chars) < 3:
        if len(chars) == 1:
            chars = "00" + chars
        chars = "0" + chars
    return chars

def has_distinct_digits(number):
    chars = str(number)

    if chars[0] != chars[1] and chars[1] != chars[2] and chars[0] != chars[2]:
        return True
    return False

def is_ascending(number):
    chars = str(number)

    if chars[0] < chars[1] and chars[1] < chars[2]:
        return True
    return False

numbers = range(0, 1000)
wanted_numbers = []
resultat = ()

for number in numbers:
    if has_distinct_digits(add_leading_zeros(number)) and is_ascending(add_leading_zeros(number)):
        wanted_numbers.append(add_leading_zeros(number))
        resultat = (", ".join(wanted_numbers))

print(resultat)
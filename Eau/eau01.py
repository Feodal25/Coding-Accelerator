desired_combinations = []

def add_leading_zeros(number):
    chars = str(number)
    while len(chars) < 2:
        chars = "0" + chars
    return chars

def get_desired_numbers():
    desired_combinations = []
    for first_number in range(0,100):
        for second_number in range(first_number + 1, 100):
                desired_combinations.append(f"{add_leading_zeros(first_number)} {add_leading_zeros(second_number)}")
    return desired_combinations

resultat = get_desired_numbers()

print((", ".join(resultat)))
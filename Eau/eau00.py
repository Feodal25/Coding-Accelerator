def get_three_digits_numbers():
    combinations = []
    for first_digit in range(0,10):
        for second_digit in range(first_digit + 1, 10):
            for third_digit in range(second_digit + 1, 10):
                combinations.append(f"{first_digit}{second_digit}{third_digit}")
    return combinations

resultat = get_three_digits_numbers()

print((", ".join(resultat)))
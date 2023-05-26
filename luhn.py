def algorithm_luhn(card_num: str) -> bool:
    """the function implements the moon algorithm, which checks 
    the validity of the card number"""
    number_card_reverse = list(map(int, card_num))[::-1]
    for i in range(1, len(number_card_reverse), 2):
        number_card_reverse[i] *= 2
        if number_card_reverse[i] > 9:
            number_card_reverse[i] = number_card_reverse[i] % 10 + \
                number_card_reverse[i] // 10
    return sum(number_card_reverse) % 10 == 0

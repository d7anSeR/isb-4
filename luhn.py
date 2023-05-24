def algorithm_luhn(card_num: str) -> bool:
    numbers = list(map(int, str(card_num)))[::-1]
    for i in range(1, len(numbers), 2):
        numbers[i] *= 2
        if numbers[i] > 9:
            numbers[i] = numbers[i] // 10 + numbers[i] % 10
    return sum(numbers) % 10 == 0
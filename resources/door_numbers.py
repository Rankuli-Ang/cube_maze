"""Module contains list of prime numbers."""
from typing import List


def get_prime_numbers() -> List[int]:
    """Creates list[int] of prime numbers from 1 to 999."""
    raw = open(r'prime_numbers.txt')
    prime_numbers_raw = raw.read().split()
    prime_numbers = []
    for number in prime_numbers_raw:
        prime_numbers.append(int(number))
    return prime_numbers


def get_non_prime_numbers(prime_numbers: list) -> List[int]:
    """Creates list[int] of non prime numbers from 1 to 999."""
    prime_numbers_length = len(prime_numbers)
    all_numbers = []
    current_number = 1
    final_number = 999
    current_prime_number_index = 0
    while current_number <= final_number:
        if current_number == prime_numbers[current_prime_number_index]:
            if current_prime_number_index + 1 < prime_numbers_length:
                current_prime_number_index += 1
            current_number += 1
        else:
            all_numbers.append(current_number)
            current_number += 1
    return all_numbers


PRIME_NUMBERS = get_prime_numbers()
NON_PRIME_NUMBERS = get_non_prime_numbers(PRIME_NUMBERS)



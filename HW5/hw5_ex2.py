from typing import Callable
from decimal import Decimal
import re

def generator_numbers(text: str):   #Функція пошуку цілих і чисел з цифрами після кому у тексті
    all_numbers = re.findall(r' \d+\.\d+ | \d+ ', text)

    for number in all_numbers:
        yield number #Генератор під кожне знайдене число 


def sum_profit(text: str, func: Callable): #Функція обрахунку загальної суми
    total = 0

    for values in func(text):
        total += Decimal(values)
        
    return total


text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів." #Тестовий текст для перевірки коду


total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
"""
Напишите функцию yes_or_no, которая принимает список из целых чисел,
проходит по нему и выводит Yes, если число уже встречалось и No, если нет
"""
from random import Random


def yes_or_no(list_numbers):
    """Проверяет список и показывает повторяется ли оно в этом списке это чис"""
    list_for_check = []
    print(list_numbers)
    for number in list_numbers:
        if isinstance(number, int):
            if number in list_for_check:
                print(f"{number} уже встречалось")
            else:
                list_for_check.append(number)
                print(f"{number} встречается в первые")
        else:
            print(f"{number} это не число")

if __name__ == '__main__':
    example_list = []
    for i in range(15):
        example_list.append(Random().randint(0, 11))

    print(example_list)

    yes_or_no(example_list)
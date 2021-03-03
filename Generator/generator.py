"""
Написать генератор get_even_number, который возвращает подряд четные числа
Например:
even_gen = get_even_number()
next(even_gen) -> 2
next(even_gen) -> 4
next(even_gen) -> 6
"""

class Get_even_number():

    """Начинает отсчёт с 0"""
    def __init__(self):
        self.start = 0

    def __iter__(self):
        return self

    """переопределили __next__ под свои требования"""
    def __next__(self): # увеличивает число на два и возвращает его
        self.start += 2
        print(self.start)


if __name__ == '__main__':
    even_get = Get_even_number()
    
    for i in range(50):
        even_get.__next__()

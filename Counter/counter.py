"""
Описать класс Counter, реализующий целочисленный счетчик.
который может увеличивать или уменьшать свое значение (атрибут value)
на единицу в заданном диапазоне.
Предусмотреть инициализацию счетчика значениями по умолчанию и произвольными значениями.
Определить атрибуты:
- value - текущее значение счетчика
Определить методы:
- инициализатор __init__, который устанавливает значение счетчика или 0 по умолчанию
- increase(num=1), увеличивает счетчик на заданную величину или 1 по умолчанию
- decrease(num=1), уменьшает счетчик на заданную величину или 1 по умолчанию
- метод __iter__
- метод __next__
"""

class Counter():

    def __init__(self, value=0):
        self.value = value
        self.list_values = [self.value]
        self.index = 0

    def increase(self, num=1) -> int:
        """увеличивает значение на заданное количество единиц
        по дефолту на 1 и вносит его в список класса"""
        self.value += num
        self.list_values.append(self.value)
        return self.value

    def decrease(self, num=1) -> int:
        """уменьшает значение на заданное количество единиц
        по дефолту на 1 и вносит его в список класса"""
        self.value -= num
        self.list_values.append(self.value)
        return self.value

    def __iter__(self):
        return self.list_values

    def __next__(self):
        """переопределяет стандартный метод для перебора списка значений
        изменения начального числа"""
        try:
            next_value = self.list_values[self.index]
            self.index += 1
            print(f"Следующее значение списка {next_value}")
        except IndexError:
            print("""Список значений закончился,
используйте метод .decrease() или .increase()""")



if __name__ == '__main__':
    number = Counter()
    print(number.decrease())
    print(number.increase())

    print(number.__iter__())

    number.__next__()
    number.__next__()
    print(number.increase(10))
    print(number.increase(-5))
    print(number.decrease(17))
    print(number.decrease(-23))
    number.__next__()
    number.__next__()
    number.__next__()
    number.__next__()
    number.__next__()
    number.__next__()
    number.__next__()
    print(number.increase(10))
    print(number.increase(-5))
    print(number.decrease(17))
    print(number.decrease(-23))
    number.__next__()
    print(number.__iter__())
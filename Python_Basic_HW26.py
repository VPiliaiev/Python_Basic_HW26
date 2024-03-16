# Створити програму-калькулятор у вигляді класу та кілька методів, як мінімум додавання,
# віднімання, ділення, множення, зведення в ступінь та вилучення квадратного кореня.
# Обернути кожен метод у блок try/except і зробити обробку кількох винятків,
# як мінімум ділення на 0.
# Створити свій виняток, наприклад, зведення в негативний ступінь.

import math


class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        try:
            return self.a + self.b
        except TypeError:
            return 'Неправильні типи аргументів'

    def sub(self):
        try:
            return self.a - self.b
        except TypeError:
            return 'Неправильні типи аргументів'

    def div(self):
        try:
            return self.a / self.b
        except ZeroDivisionError:
            return 'Ділення на нуль неможливе'
        except TypeError:
            return 'Неправильні типи аргументів'

    def mul(self):
        try:
            return self.a * self.b
        except TypeError:
            return 'Неправильні типи аргументів'

    def power(self):
        try:
            return math.pow(self.a, self.b)
        except ValueError:
            return 'Неправильний аргумент для зведення в ступінь'
        except TypeError:
            return 'Неправильні типи аргументів'

    def square_root(self):
        try:
            if self.a < 0:
                raise ValueError("Квадратний корінь можна вилучити тільки з не від'ємних чисел")
            return math.sqrt(self.a)
        except ValueError as i:
            return str(i)
        except TypeError:
            return "Неправильні типи аргументів"

counting = Calculator (2,2)
print('Додавання:', counting.add())
print('Віднімання:', counting.sub())
print('Ділення:', counting.div())
print('Множення:', counting.mul())
print('Зведення в ступінь:', counting.power())
print('Вилучення квадратного кореня:', counting.square_root())
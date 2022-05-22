class ZeroDivision(Exception):

    def __init__(self, text):
        self.text = text


a = int(input(f'Введите первое число: '))
b = int(input(f'Введите второе число: '))

try:
    print(a / b)
except ZeroDivisionError:
    print(ZeroDivision('Деление на ноль невозможно'))


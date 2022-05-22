class Value(Exception):

    def __init__(self, text):
        self.text = text


some_list = []
while True:
    a = input(f'Внесите число в список: ')
    if a == 'stop':
        break
    else:
        try:
            some_list.append(int(a))
        except ValueError:
            print(Value(f'Значение неверно, вводите только числа!'))
print(some_list)

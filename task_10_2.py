class Clothes:

    def __init__(self, attr, value):
        self.attr = attr
        self.value = value
        if self.attr == 'coat':
            coat_cloth = value/6.5 + 0.5
            print(f'Расход ткани на пальто равен {coat_cloth}')
        if self.attr == 'suit':
            suit_cloth = 2 * value + 0.3
            print(f'Расход ткани на костюм равен {suit_cloth}')

    def __add__(self, other):
        if self.attr == 'coat':
            some_str = f'Общий расход ткани = {(self.value/6.5 + 0.5) + (2 * other.value + 0.3)}'
            return some_str
        if self.attr == 'suit':
            some_str = f'Общий расход ткани = {(other.value / 6.5 + 0.5) + (2 * self.value + 0.3)}'
            return some_str

    @property
    def my_method(self):
        return f'Декоратор работает. {self.attr, self.value}'


a = Clothes('coat', 36)
b = Clothes('suit', 178)
print(b+a)
print(a.my_method)

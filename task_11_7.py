class ComplexNumber:

    def __init__(self, number):
        self.number = number

    def __add__(self, other):
        return self.number + other.number

    def __mul__(self, other):
        return self.number * other.number


a = ComplexNumber(386)
b = ComplexNumber(819)
print(a + b)
print(a * b)
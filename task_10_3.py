class Cell:

    def __init__(self, cells: int):
        self.cells = cells

    def __add__(self, other):
        return self.cells + other.cells

    def __sub__(self, other):
        if self.cells - other.cells > 0:
            return self.cells - other.cells
        else:
            return f'Вычитание невозможно'

    def __mul__(self, other):
        return self.cells * other.cells

    def __floordiv__(self, other):
        return self.cells // other.cells

    def __truediv__(self, other):
        return self.cells / other.cells

    def make_order(self, value):
        line = str()
        cells_in_line = self.cells
        while cells_in_line // value > 0:
            line = line + f'{"*" * value}\\n'
            cells_in_line -= value
        line = line + f'{"*" * cells_in_line}\\n'
        print(line)


a = Cell(15)
b = Cell(83)
print(a + b)
print(a - b)
print(a * b)
print(a // b)
print(a / b)
a.make_order(2)

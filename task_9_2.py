class Road:
    _lenght = 1000
    _width = 15

    def mass(self):
        real_mass = self._lenght * self._width * 25 * 5
        print(f'Расчетная масса аcфальта - {real_mass} тонн')


a = Road()
a._lenght = 1500
a._width = 25
a.mass()
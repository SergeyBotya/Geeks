class Stationery:
    title = 'Название'

    def draw(self):
        print('Запуск отрисовки.')


class Pen(Stationery):
    def draw(self):
        print('Рисунок ручкой получается чётким, и его нельзя стереть.')


class Pencil(Stationery):
    def draw(self):
        print('Рисунок карандашом не так хорошо видно, но зать его можно стереть и исправить ошибку.')


class Marker(Stationery):
    def draw(self):
        print("Жирный, фиг сотрёшь.")


a = Stationery()
a.draw()

a = Pen()
a.draw()

a = Pencil()
a.draw()

a = Marker()
a.draw()
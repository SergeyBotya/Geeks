class Car:
    speed = 90
    colour = 'green'
    name = 'Porsche'
    is_police = False

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction: str):
        print(f'Машина повернула {direction}')

    def show_speed(self):
        print(f'Машина едет со скоростью {self.speed} км/ч')


class TownCar(Car):
    def show_speed(self):
        if self.speed >= 60:
            print("Скорость превышена! Сбавьте скорость.")
        else:
            print(f'Машина едет со скоростью {self.speed} км/ч')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed >= 40:
            print("Скорость превышена! Сбавьте скорость.")
        else:
            print(f'Машина едет со скоростью {self.speed} км/ч')


class PoliceCar(Car):
    pass


a = TownCar()
a.speed = 85
a.go()
a.stop()
a.turn('налево')
a.show_speed()

b = WorkCar()
b.speed = 39
b.show_speed()
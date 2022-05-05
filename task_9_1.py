import time


class Trafficlight:
    __colour = ['Красный', 'Жёлтый', 'Зелёный']

    def running(self):
        while True:
            print(f'Включаем {self.__colour[0]} свет')
            time.sleep(7)
            print(f'Включаем {self.__colour[1]} свет')
            time.sleep(2)
            print(f'Включаем {self.__colour[2]} свет')
            time.sleep(5)


a = Trafficlight()
a.running()
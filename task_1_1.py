#Реализовать вывод информации о промежутке времени в зависимости от его
#продолжительности duration в секундах:

duration = input('Введите время в секундах: ')

if int(duration) < 0:
    print('Число указано неверно. Перезапустите программу и укажите верное количество секунд.')

elif int(duration) <= 59:
    print(f'{duration} сек')

elif 59 < int(duration) <= 3599:
    minutes = int(duration) // 60
    seconds = int(duration) % 60
    print(f'{minutes} мин {seconds} сек')

elif 3599 < int(duration) <= 86399:
    hours = int(duration) // 3600
    minutes = (int(duration) - (hours * 3600)) // 60
    seconds = int(duration) % 60
    print(f'{hours} час {minutes} мин {seconds} сек')

else:
    days = int(duration) // 86400
    hours = (int(duration) - (days * 86400)) // 3600
    minutes = (int(duration) - (days * 86400) - (hours * 3600)) // 60
    seconds = int(duration) % 60
    print(f'{days} дн {hours} час {minutes} мин {seconds} сек')
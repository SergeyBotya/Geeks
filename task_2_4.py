workers = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА',
'токарь высшего разряда нИКОЛАй', 'директор аэлита']

for i in range(len(workers)):
    name = (workers[i].split()[-1].title())
    print(f'Привет, {name}!')


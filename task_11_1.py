class Date:
    def __init__(self, date: str):
        self.date = date

    @classmethod
    def class_method(cls, date: str):
        date_list = date.split('-')
        day = int(date_list[0])
        month = int(date_list[1])
        year = int(date_list[2])
        print(f'Число - {day}, месяц - {month}, год - {year}')

    @staticmethod
    def static_method(date: str):
        date_list = date.split('-')
        day = int(date_list[0])
        month = int(date_list[1])
        year = int(date_list[2])
        if 0 < month < 13 and year > 0:
            if year % 4 == 0 and year % 100 != 0:
                if month == 2:
                    if day > 29 or day < 0:
                        print('Дата указана неверно')
                    else:
                        print('Дата указана верно')
                elif month == 4 or month == 6 or month == 9 or month == 11:
                    if day > 30 or day < 0:
                        print('Дата указана неверно')
                    else:
                        print('Дата указана верно')
                else:
                    if day < 0 or day > 31:
                        print('Дата указана неверно')
                    else:
                        print('Дата указана верно')
            elif year % 400 == 0 and year % 100 == 0:
                if month == 2:
                    if day > 29 or day < 0:
                        print('Дата указана неверно')
                    else:
                        print('Дата указана верно')
                elif month == 4 or month == 6 or month == 9 or month == 11:
                    if day > 30 or day < 0:
                        print('Дата указана неверно')
                    else:
                        print('Дата указана верно')
                else:
                    if day < 0 or day > 31:
                        print('Дата указана неверно')
                    else:
                        print('Дата указана верно')
            elif month == 4 or month == 6 or month == 9 or month == 11:
                if day > 30 or day < 0:
                    print('Дата указана неверно')
                else:
                    print('Дата указана верно')
            elif month == 2:
                if day > 29 or day < 0:
                    print('Дата указана неверно')
                else:
                    print('Дата указана верно')
            else:
                if day > 31 or day < 0:
                    print('Дата указана неверно')
                else:
                    print("Дата указана верно")
        else:
            print('Дата указана неверно')


Date.class_method('15-03-2008')
Date.static_method('31-13-2021')
a = Date('18-12-2015')
a.class_method('18-12-2015')

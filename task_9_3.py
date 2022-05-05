class Worker:
    name = 'name'
    surname = 'surname'
    position = 'position'
    income = 'income'
    _wage_bonus = {"wage": 'wage', "bonus": 'bonus'}


class Position(Worker):

    def get_full_name(self):
        print(f'Сотрудник - {self.name} {self.surname}')

    def get_total_income(self):
        print(f'Общий доход - {self.income}, из него:\n'
              f'Оклад - {self._wage_bonus["wage"]}, бонус - {self._wage_bonus["bonus"]}')


a = Position()
a.name = 'Игорь'
a.surname = 'Петров'
a.income = 350000
a._wage_bonus = {"wage": 200000, "bonus": 150000}
a.get_full_name()
a.get_total_income()
our_warehouse = set()


class Warehouse:
    def __init__(self, name, warehouse: set):
        self.name = name
        self.warehouse = warehouse
        self.warehouse.add(self)


class OfficeEquipment:
    def __init__(self, model: str, count: int):
        self.model = model
        self.count = count
        if type(self.count) != int:
            print('Вы указали неправильное количество техники. Введите число')
            pass

    def __str__(self):
        return f'{self.model}, {self.count}'


class Printer(OfficeEquipment):
    def __init__(self, model, count, param_1, param_2):
        super().__init__(model, count)
        self.param1 = param_1
        self.param2 = param_2


class Scanner(OfficeEquipment):
    def __init__(self, model, count, param_1, param_2):
        super().__init__(model, count)
        self.param1 = param_1
        self.param2 = param_2


class Xerox(OfficeEquipment):
    def __init__(self, model, count, param_1, param_2):
        super().__init__(model, count)
        self.param1 = param_1
        self.param2 = param_2


a = Printer("sky scanner", 45, 'blue', 318)
print(a)
load = Warehouse(a, our_warehouse)
print(our_warehouse)

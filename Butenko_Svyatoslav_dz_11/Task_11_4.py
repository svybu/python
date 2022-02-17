class Storage:
    def __init__(self, name, amount, price):
        self.name = name
        self.amount = amount
        self.price = price
        self.units = {'Модель': self.name, 'Количество': self.amount, 'Цена': self.price}


    def receiving(self):
        try:
            self.units['Количество'] = self.units.get('Количество') + int(input('Введите количеcтво полученных устройств ')) + self.amount
            return f'На складе осталось {self.units} единиц'
        except:
            return f'Ошыбка ввода'
    def giving(self):
        try:
            self.units['Количество'] = self.amount + self.units.get('Количество') - int(input('Введите количеcтво полученных устройств '))
            return f'На складе осталось {self.units} единиц'
        except:
            return f'Ошыбка ввода'


class Printer(Storage):
    def to_print(self):
        return f'I can print'

class Scanner(Storage):
    def to_print(self):
        return f'I can print'

class Copier(Storage):
    def to_print(self):
        return f'I can print'

a = Printer('Samsung', 5, 10)
a.receiving()

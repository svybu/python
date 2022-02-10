class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'Запуск отрисовки'

class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Это рисует ручка'


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Это рисует карандаш'

class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Это рисует маркер'

a = Pen('parker')
b = Pencil('крандаш')
d = Handle('маркер')
print(a.draw())
print(b.draw())
print(d.draw())
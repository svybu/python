class Cell:
    def __init__(self, subcell):
        self.subcell = int(subcell)


    def __add__(self, other):
        return Cell(self.subcell + other.subcell)

    def __sub__(self, other):
        return self.subcell - other.subcell if (self.subcell - other.subcell) > 0 else print('Отрицательно значение')

    def __mul__(self, other):
        return Cell(self.subcell * other.subcell)

    def __truediv__(self, other):
        return Cell(self.subcell // other.subcell)

    def make_order(self, el_in_line):
        line = ''
        for i in range(int(self.subcell / el_in_line)):
            line += f'{"*" * el_in_line} \\n'
        line += f'{"*" * (self.subcell % el_in_line)}'
        return line

a = Cell(40)
b = Cell(20)
c = a + b
print(f'результат сложения {c.subcell}')
c = a - b
print(f'результат вычитания {c}')
c = a * b
print(f'результат умножения {c.subcell}')
c = a / b
print(f'результат деления {c.subcell}')
print(a.make_order(10))

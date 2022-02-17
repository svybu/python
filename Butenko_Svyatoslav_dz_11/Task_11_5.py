class Complex_Number:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.number = 'a +b*i'

    def __add__(self, other):
        return f'Cумма равна {self.a + other.a} + {self.b + other.b}*i '

    def __mul__(self, other):
        result = (self.a * other.a - self.b * other.b) + (self.a * other.b - other.a * self.b)
        return f'Результат умножения равен {result}*i'

numb_1 = Complex_Number(2, 5)
numb_2 = Complex_Number(1, 4)
print(numb_1 * numb_2)
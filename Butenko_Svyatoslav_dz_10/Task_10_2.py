class Cloth:
    def __init__(self, size, hight):
        self.size = size
        self.hight = hight

    @property
    def coat_square(self):
        return self.size/6.5+0.5

    @property
    def costume_square(self):
        return self.hight*2+0.3

    def full_square(self):
        return self.coat_square + self.costume_square


class Coat(Cloth):
    def __init__(self, size):
        super().__init__(size, None)

    @property
    def coat_square(self):
        return round(self.size / 6.5 + 0.5)


class Costume(Cloth):
    def __init__(self, hight):
        super().__init__(0,  hight)

    @property
    def costume_square(self):
        return round(self.hight * 2 + 0.3)

coat = Coat(50)
costume = Costume(10)
a = coat.coat_square + costume.costume_square
print(a)

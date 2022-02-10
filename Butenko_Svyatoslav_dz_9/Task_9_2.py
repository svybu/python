class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calculations(self):
        mass = self._length * self._width * 25 * 5
        print(mass)
        #return (mass)


a = Road(5000, 200)
a.calculations()
import time

class TrafficLight:
    _colors = {'red': 7, 'yellow':2, 'green':7}
    _color = ''

    def __init__(self, _color):
        self._color = _color


    def running(self, _color):
        for color, colortime in self._colors:
            self.time = colortime
            print(f'{self._color} for {self.time} seconds')
            time.sleep(colortime)

a = TrafficLight({'red': 7, 'yellow': 2, 'green': 7})
print(a.running)

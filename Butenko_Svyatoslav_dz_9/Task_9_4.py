class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} is starting'
    def stop(self):
        return f'{self.name} is stopping'
    def turn(self, direction):
        return f'{self.name} is turning {direction}'
    def show_speed(self):
        return f'{self.name} speed is {self.speed}'

class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print( f'{self.name} speed is {self.speed}')

        if self.speed > 60:
            return f'{self.speed} is more than allowed 60'

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print( f'{self.name} speed is {self.speed}')

        if self.speed > 60:
            return f'{self.speed} is more than allowed 60'

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

ford = TownCar(80, 'blue', 'ford', False)
print(ford.show_speed())
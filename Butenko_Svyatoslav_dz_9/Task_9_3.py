class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}

class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        full_name = self.name+ ' ' +  self.surname
        return(full_name)

    def get_total_income(self):
        total_income = self._income.get('wage') + self._income.get('bonus')
        return (total_income)

Petrovich = Position('Petro', 'Petrovich', 'engineer', 5000, 1000)
print(Petrovich.get_full_name())
print(Petrovich.get_total_income())

class DivideByZero:
    def __init__(self, divided, divider):
        self.devided = divided
        self.devider = divider

    @staticmethod
    def dividing(divided, divider):
        try:
            return (divided/divider)
        except:
            return f'Sorry, I can not divide this'
a = DivideByZero(10, 5)
print(a.dividing(10,0))
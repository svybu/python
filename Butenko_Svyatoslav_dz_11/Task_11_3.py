class Only_Numbers:
    def __init__(self):
        self.numbers_list = []

    def the_input(self):
        self.numbers_list = []
        while True:
            try:
                number = int(input('Введите число. Чтобы прекратить ввод - введите stop'))
                self.numbers_list.append(number)
                print(self.numbers_list)
            except:
                print('Недопустимое значение')
                if number == 'stop':
                    break

a = Only_Numbers
a.the_input()
class Data:
    def __init__(self, text_date):
        self.text_date = text_date

    @classmethod
    def extract(cls, text_date):
        text_date = text_date.split('-')
        return text_date

    @staticmethod
    def validation(text_date):
        day = int(text_date[0])
        month = int(text_date[1])
        year = int(text_date[2])
        if 1<= day <= 31:
            if 1<= month <= 12:
                if year >= 0:
                    return f'{day}, {month}, {year} A.D'
                else:
                    return f'{day}, {month}, {year} B.C.'
            else:
                return f'Wrong month'
        else:
            return f'Wrong day'

a = Data('09-02-2022')
a = a.extract('09-02-2022')
print(Data.validation(a))

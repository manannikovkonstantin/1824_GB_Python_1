import datetime

class Date:
    __date = None

    def __init__(self, data):
        self._data = str(data)

    @classmethod
    def date_int(cls, date):
        day, month, year = date.split('-')
        cls.__date = tuple(map(int, [year, month, day]))
        return cls.__date

    @staticmethod
    def valid_date(date):
        item = True
        try:
            datetime.datetime(*date)
        except ValueError:
            item = False

        if item:
            print("Input date is valid.")
        else:
            print("Input date is not valid.")

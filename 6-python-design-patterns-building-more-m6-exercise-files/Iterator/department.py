class Department:
    def __init__(self, number, name, date):
        self._number = number
        self._name = name
        self._date = date

    @property
    def number(self):
        return self._number

    @property
    def name(self):
        return self._name

    @property
    def date(self):
        return self._date

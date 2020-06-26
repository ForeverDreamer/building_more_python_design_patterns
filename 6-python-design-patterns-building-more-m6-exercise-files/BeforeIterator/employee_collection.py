class Employees:

    def __init__(self):
        self._headcount = 0
        self._employees = {}

    def add_employee(self, employee):
        self._headcount += 1
        self._employees[self._headcount] = employee

    def get_employee(self, i):
        return self._employees[i]

    @property
    def headcount(self):
        return self._headcount

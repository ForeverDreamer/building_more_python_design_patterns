from collections import Iterable


class Employees(Iterable):

    def __init__(self):
        self._headcount = 0
        self._employees = {}

    def add_employee(self, employee):
        self._headcount += 1
        self._employees[self._headcount] = employee

    def __iter__(self):
        return (e for e in self._employees.values())

from collections import Iterator


class Employees(Iterator):

    def __init__(self):
        self._employees = {}
        self._headcount = 0
        self._curr_id = 0

    def add_employee(self, employee):
        self._headcount += 1
        self._employees[self._headcount] = employee

    def __iter__(self):
        self._curr_id = 0
        return self

    def __next__(self):
        if self._curr_id < self._headcount:
            self._curr_id += 1
            return self._employees[self._curr_id]
        else:
            raise StopIteration

from collections import Iterable, Iterator


class Employees(Iterable):

    def __init__(self):
        self._employees = {}
        self._headcount = 0

    def add_employee(self, employee):
        self._headcount += 1
        self._employees[self._headcount] = employee

    def __iter__(self):
        return EmployeesIterator(self._employees, self._headcount)


class EmployeesIterator(Iterator):
    def __init__(self, employees, headcount):
        self._employees = employees
        self._headcount = headcount
        self._curr_id = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._curr_id < self._headcount:
            self._curr_id += 1
            return self._employees[self._curr_id]
        else:
            raise StopIteration

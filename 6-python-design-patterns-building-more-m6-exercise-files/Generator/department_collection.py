from collections import Iterable


class Departments(Iterable):

    def __init__(self):
        self._departments = []

    def add_department(self, department):
        self._departments.append(department)

    def __iter__(self):
        return (d for d in self._departments)

from collections import Sequence


class Departments(Sequence):

    def __init__(self):
        self._departments = []

    def add_department(self, department):
        self._departments.append(department)

    def __getitem__(self, idx):
        return self._departments[idx]

    def __len__(self):
        return len(self._departments)

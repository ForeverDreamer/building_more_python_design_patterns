from abc import ABC, abstractmethod


class AbsEmployees(ABC):

    @abstractmethod
    def get_employee_info(self, empids):
        pass

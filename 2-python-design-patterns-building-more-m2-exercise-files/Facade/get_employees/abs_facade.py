from abc import ABC, abstractmethod


class AbsFacade(ABC):

    @abstractmethod
    def get_employees(self):
        pass

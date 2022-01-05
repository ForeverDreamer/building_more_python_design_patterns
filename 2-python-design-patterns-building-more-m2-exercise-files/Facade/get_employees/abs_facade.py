from abc import ABC, abstractmethod


class AbsFacade(ABC):

    @abstractmethod
    def get_employees(self):
        pass

    @abstractmethod
    def create_employees(self):
        pass

    @abstractmethod
    def update_employees(self):
        pass
    
    @abstractmethod
    def delete_employees(self):
        pass

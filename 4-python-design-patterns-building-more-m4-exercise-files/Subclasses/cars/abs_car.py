from abc import ABC, abstractmethod


class AbsCar(ABC):
    @property
    @abstractmethod
    def description(self):
        pass

    @property
    @abstractmethod
    def cost(self):
        pass

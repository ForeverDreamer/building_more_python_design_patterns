from abc import ABC, abstractmethod


class AbsCar(ABC):

    @property
    @abstractmethod
    def description(self):
        pass

    @property
    @abstractmethod
    def engine(self):
        pass

    @property
    @abstractmethod
    def paint(self):
        pass

    @property
    @abstractmethod
    def upholstery(self):
        pass

    def cost(self):
        cost = 0.00
        if self.engine == '4 cyl':
            cost += 0.00
        elif self.engine == '6 cyl':
            cost += 1500.00
        if self.paint == 'white':
            cost += 0.00
        elif self.paint == 'black':
            cost += 1000.00
        elif self.paint == 'red':
            cost += 2000.00
        if self.upholstery == 'vinyl':
            cost += 0.00
        elif self.upholstery == 'leather':
            cost += 2000.00
        return cost

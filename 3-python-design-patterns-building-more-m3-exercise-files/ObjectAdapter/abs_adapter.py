from abc import ABC, abstractmethod


class AbsAdapter(ABC):

    def __init__(self, adaptee):
        self._adaptee = adaptee

    @property
    def adaptee(self):
        return self._adaptee

    @property
    @abstractmethod
    def name(self):
        pass

    @property
    @abstractmethod
    def address(self):
        pass

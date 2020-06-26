from abc import ABC, abstractmethod


class AbsState(ABC):

    def __init__(self, context):
        self._cart = context

    @abstractmethod
    def add_item(self):
        pass

    @abstractmethod
    def remove_item(self):
        pass

    @abstractmethod
    def checkout(self):
        pass

    @abstractmethod
    def pay(self):
        pass

    @abstractmethod
    def empty_cart(self):
        pass

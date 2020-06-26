from abc import ABC, abstractmethod


class AbsComposite(ABC):

    @abstractmethod
    def get_oldest(self):
        pass

from abc import ABC, abstractmethod

class Coffee(ABC):

    @abstractmethod
    def coffee_type(self):
        pass
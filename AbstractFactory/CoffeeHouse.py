from abc import ABC, abstractmethod

class CoffeeHouse(ABC):

    @abstractmethod
    def produce_coffee(self):
        pass

    @abstractmethod
    def produce_tea(self):
        pass

    @abstractmethod
    def produce_food(self):
        pass

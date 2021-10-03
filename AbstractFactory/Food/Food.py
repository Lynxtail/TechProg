from abc import ABC, abstractmethod

class Food(ABC):

    def __init__(self, weight):
        self.__weight = weight

    @abstractmethod
    def weight(self):
        pass
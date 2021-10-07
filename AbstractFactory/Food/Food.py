from abc import ABC, abstractmethod

class Food(ABC):

    # def __init__(self, weight):
    #     self.__weight = weight

    @abstractmethod
    def food_type(self):
        pass

    @abstractmethod
    def get_info(self):
        pass
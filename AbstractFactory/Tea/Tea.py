from abc import ABC, abstractmethod

class Tea(ABC):

    def __init__(self, volume):
        self.__volume = volume
        
    @abstractmethod
    def tea_type(self):
        pass
from abc import ABC, abstractmethod

class Coffee(ABC):

    def __init__(self, milk):
        if milk == 'with milk':
            self.__milk = milk
        elif milk == 'without milk':
            self.__milk = 'without milk'
        else:
            print("I don't know that type of coffee")
        
    @abstractmethod
    def coffee_type(self):
        pass

    def get_info(self):
        print(f'{self.coffee_type}, {self.__milk}')
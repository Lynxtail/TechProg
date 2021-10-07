from .Food import Food

class Cookies(Food):
    __type = 'Cookies'
    # __weight = 0

    def __init__(self, weight= 50):
        self.__weight = weight

    @property
    def food_type(self):
        return self.__type

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        if weight >= 0:
            self.__weight = weight
        else:
            print("Incorrect weight!")
    
    def get_info(self):
        print(f'{self.food_type}, {self.weight} mg')
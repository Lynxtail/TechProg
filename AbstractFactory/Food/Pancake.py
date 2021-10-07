from .Food import Food

class Pancake(Food):
    __type = 'Pancake'
    # __weight = 0
    # __filling = ''

    def __init__(self, weight= 150, filling= 'honey'):
        self.__weight = weight
        self.__filling = filling

    @property
    def food_type(self):
        return self.__type

    @property
    def filling(self):
        return self.__filling

    @filling.setter
    def filling(self, filling):
        self.__filling = filling

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        if weight >= 0:
            self.__weight = weight
        else:
            print("Отрицательный вес невозможен")

    def get_info(self):
        print(f'{self.food_type}, with {self.filling}, {self.weight} mg')
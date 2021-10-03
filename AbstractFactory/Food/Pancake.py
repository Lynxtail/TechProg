from Food import Food

class Pancake(Food):

    def __init__(self, weight, filling):
        super().__init__()
        self.__filling = filling

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
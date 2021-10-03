from Food import Food

class Cookies(Food):

    def something(self):
        pass

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        if weight >= 0:
            self.__weight = weight
        else:
            print("Отрицательный вес невозможен")
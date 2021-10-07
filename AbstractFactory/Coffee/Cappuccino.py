from .Coffee import Coffee

class Cappuccino(Coffee):
    __type = 'Cappuccino'

    def __init__(self, milk= 'with milk'):
        super().__init__(milk)

    @property
    def coffee_type(self):
        return self.__type
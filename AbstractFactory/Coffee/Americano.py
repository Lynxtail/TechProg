from .Coffee import Coffee

class Americano(Coffee):
    __type = 'Americano'

    def __init__(self, milk= 'without milk'):
        super().__init__(milk)

    @property
    def coffee_type(self):
        return self.__type
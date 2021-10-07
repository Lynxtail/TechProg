from .Tea import Tea

class GreenTea(Tea):
    __type = 'Green Tea'

    def __init__(self, volume= 250):
        super().__init__(volume)
    
    @property
    def tea_type(self):
        return self.__type
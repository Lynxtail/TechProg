from .Tea import Tea

class BlackTea(Tea):
    __type = 'Black Tea'

    def __init__(self, volume= 250):
        super().__init__(volume)
    
    @property
    def tea_type(self):
        return self.__type
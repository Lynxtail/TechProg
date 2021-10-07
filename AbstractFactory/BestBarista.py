from Coffee.Cappuccino import Cappuccino
from Food.Cookies import Cookies
from Tea.BlackTea import BlackTea
from CoffeeHouse import CoffeeHouse

class BestBarista(CoffeeHouse):
    def produce_coffee(self):
        return Cappuccino()
    
    def produce_tea(self):
        return BlackTea()

    def produce_food(self):
        return Cookies()
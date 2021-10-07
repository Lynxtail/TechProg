from Coffee.Americano import Americano
from Food.Pancake import Pancake
from Tea.GreenTea import GreenTea
from CoffeeHouse import CoffeeHouse

class CoffeeOnTheRoad(CoffeeHouse):
    def produce_coffee(self):
        return Americano()
    
    def produce_tea(self):
        return GreenTea()

    def produce_food(self):
        return Pancake()
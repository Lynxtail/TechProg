from abc import ABC, abstractmethod

class Builder(ABC):
  
  @property
  @abstractmethod
  def product(self):
    pass
  
  @abstractmethod
  def add_water(self):
    pass

  @abstractmethod
  def add_milk(self):
    pass

  @abstractmethod
  def add_coffee(self):
    pass
    
  @abstractmethod
  def add_tea(self):
    pass
 
class Barista(Builder):
  def __init__(self):
    self.reset()

  def reset(self):
    self._product = Product()

  @property
  def product(self):
    product = self._product
    self.reset()
    return product

  def add_coffee(self):
    self._product.add('Coffee')
  
  def add_water(self):
    self._product.add('Water')
  
  def add_milk(self):
    self._product.add('Milk')

  def add_tea(self):
    self._product.add('Tea')

class Product:

  def __init__(self):
    self.parts = []

  def add(self, part):
    self.parts.append(part)

  def list_parts(self):
    print(f"Product consits: {', '.join(self.parts)}", end='\n')

class Director:

    def __init__(self):
     self._builder = None

    @property
    def builder(self):
      return self._builder

    @builder.setter
    def builder(self, builder: Builder):
      self._builder = builder

    def produce_americano(self):
        self._builder.add_coffee()
        self._builder.add_water()

    def produce_cappuccino(self):
        self._builder.add_coffee()
        self._builder.add_milk()

    def produce_tea(self):
        self._builder.add_tea()
        self._builder.add_water()

    def produce_tea_with_milk(self):
        self._builder.add_tea()
        self._builder.add_milk()
        self._builder.add_water()

if __name__ == "__main__":
  director = Director()
  builder = Barista()
  director.builder = builder

  #варим чай
  print("List of tea: ")
  director.produce_tea()
  builder._product.list_parts()
  builder.reset()
  director.produce_tea_with_milk()
  builder._product.list_parts()

  #варим кофе
  print("\n\nList of coffee: ")
  builder.reset()
  director.produce_cappuccino()
  builder._product.list_parts()
  builder.reset()
  director.produce_americano()
  builder._product.list_parts()


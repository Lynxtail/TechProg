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

class Product:

  def __init__(self):
    self.parts = []

  def add(self, part):
    self.parts.append(part)

  def list_parts(self):
    print(f"Product consits: {', '.join(self.parts)}", end='')  

class Barista(Builder):
  def __init__(self):
    self.reset()

  def reset(self):
    self.product = Product()

  @property
  def product(self):
    product = self.product
    self.reset()
    return product

  def add_coffee(self):
    self.product.add('Coffee')
  
  def add_water(self):
    self.product.add('Water')
  
  def add_milk(self):
    self.product.add('Milk')

  def add_tea(self):
    self.product.add('Tea')

# class Director:

    def __init__(self):
     self.builder = None

    @property
    def builder(self):
      return self.builder

    @builder.setter
    def builder(self, builder: Builder):
      self.builder = builder

    def produce_americano(self):
        self.builder.add_coffee()
        self.builder.add_water()

    def produce_cappuccino(self):
        self.builder.add_coffee()
        self.builder.add_milk()

    def produce_tea(self):
        self.builder.add_tea()
        self.builder.add_water()

    def produce_tea_with_milk(self):
        self.builder.add_tea()
        self.builder.add_milk()
        self.builder.add_water()

if __name__ == "__main__":
  # director = Director()
  builder = Barista()
  # director.builder = builder

  #варим чай
  print("List of tea: ")
  # director.produce_tea()
  builder.add_tea()
  builder.add_water()
  builder.product.list_parts()
  # director.produce_tea_with_milk()
  # builder.product.list_parts()

  #варим кофе
  print("List of coffee: ")
  # director.produce_cappuccino()
  builder.add_coffee()
  builder.add_water()
  builder.add_milk()
  builder.product.list_parts()
  # director.produce_americano()
  # builder.product.list_parts()


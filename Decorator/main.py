class Product():
    def get_info(self):
        pass

class BaseProduct(Product):
    def get_info(self):
        return "Base model of product has been created"

class Decorator(Product):
    _product: Product = None

    def __init__(self, product: Product):
        self._product = product

    @property
    def product(self):
        return self._product

    def get_info(self):
        return self._product.get_info()


class DeveloperA(Decorator):
    def get_info(self):
        return f"{self.product.get_info()} (modified by Developer A)"

class DeveloperB(Decorator):
    def get_info(self):
        return f"{self.product.get_info()} (modified by Developer B)"

def client_code(product: Product):
    print(f"{product.get_info()}")

if __name__ == "__main__":
    ordinary_prod = BaseProduct()
    print("Base order: ")
    client_code(ordinary_prod)
    print()

    decorator1 = DeveloperA(ordinary_prod)
    decorator2 = DeveloperB(ordinary_prod)
    decorator3 = DeveloperB(decorator1)
    print("Personal order: ")
    client_code(decorator1)
    client_code(decorator2)
    client_code(decorator3)
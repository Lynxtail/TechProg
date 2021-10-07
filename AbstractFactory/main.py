from CoffeeHouse import CoffeeHouse
from BestBarista import BestBarista
from CoffeeOnTheRoad import CoffeeOnTheRoad

def create_order(factory: CoffeeHouse):
    order = []
    n = int(input("Enter the number of positions: "))
    for _ in range(n):
        ans = input("Do you wish coffee [c], tea [t], or some food [f]? ")
        if ans == 'c':
            order.append(factory.produce_coffee())
        elif ans == 't':
            order.append(factory.produce_tea())
        elif ans == 'f':
            order.append(factory.produce_food())
        else:
            print("There's some error, please call the admin!")
    return order

def list_of_orders(orders):
    i = 1
    print('_'*10)
    for item in orders:
        print(f'\nOrder {i}:')
        for pos in item:
            pos.get_info()
        i += 1

if __name__ == "__main__":
    orders = []
    orders.append(create_order(BestBarista()))
    orders.append(create_order(CoffeeOnTheRoad()))
    list_of_orders(orders)

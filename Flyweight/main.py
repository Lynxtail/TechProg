import json

class Flyweight():
    
    def __init__(self, shared_state):
        self._shared_state = shared_state

    def operation(self, unique_state):
        s = json.dumps(self._shared_state)
        u = json.dumps(unique_state)
        print(f"Внешний вид: {s}\nИнформация: {u}")


class FlyweightFactory():

    _flyweights = {}

    def __init__(self, initial_flyweights):
        for state in initial_flyweights:
            self._flyweights[self.get_key(state)] = Flyweight(state)

    def get_key(self, state):
        return "_".join(sorted(state))

    def get_flyweight(self, shared_state):
        key = self.get_key(shared_state)

        if not self._flyweights.get(key):
            print("Нет подходящего шаблона, создаётся новый.")
            self._flyweights[key] = Flyweight(shared_state)
        else:
            print("Использование существующего шаблона.")

        return self._flyweights[key]

    def list_flyweights(self):
        count = len(self._flyweights)
        print(f"Имеется {count} единиц:")
        print("\n".join(map(str, self._flyweights.keys())), end="")


def add_book(factory, publisher, version, author, title):
    print("\nДобавление книги в базу:")
    flyweight = factory.get_flyweight([publisher, version])
    flyweight.operation([author, title])


if __name__ == "__main__":
    
    factory = FlyweightFactory([ 
        ["AST", "e-book"],
        ["MIF", "hardcover"],
        ["MIF", "softcover"],
        ["Azbuka", "softcover"]])

    factory.list_flyweights()

    add_book(factory, "AST", "hardcover", "G. R. R. Martin", "A Game of Thrones")
    add_book(factory, "AST", "e-book", "J. R. R. Tolkien", "The Lord of the Rings")
    print()
    factory.list_flyweights()
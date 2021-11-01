import random
class Sorter:
    garbage = ['bottle', 'bag', 'package', 'scrap', 'battery']

    def __init__(self, subsystem1, subsystem2):
        self._subsystem1 = subsystem1
        self._subsystem2 = subsystem2

    def operation(self) -> str:
        results = []
        results.append("Sorter ready to work!")
        results.append(self._subsystem1.operation(random.choice(self.garbage)))
        results.append(self._subsystem2.operation(random.choice(self.garbage)))
        return "\n".join(results)


class Utilization:    
    def operation(self, object) -> str:
        return f"Object {object} was utilized"

class Recycling:
    def operation(self, object) -> str:
        return f"Object {object} was recycled"


def client_code(sorter: Sorter):
    print(sorter.operation(), end="")


if __name__ == "__main__":
    subsystem1 = Utilization()
    subsystem2 = Recycling()
    facade = Sorter(subsystem1, subsystem2)
    client_code(facade)
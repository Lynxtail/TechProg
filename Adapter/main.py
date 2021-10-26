class Target:
    def request(self) -> str:
        return "Target: The default target's behavior."

# получает на вход чистую строку
class Back:
    _descrypt = ''
    def specific_request(self) -> str:
        return self._descrypt

# расшифровывает строку
class Encrypter(Target, Back):
    
    def request(self) -> str:
        return 


def client_code(target: "Target") -> None:
    """
    Клиентский код поддерживает все классы, использующие интерфейс Target.
    """

    print(target.request(), end="")


if __name__ == "__main__":
    print("Client: I can work just fine with the Target objects:")
    target = Target()
    client_code(target)
    print("\n")

    adaptee = Adaptee()
    print("Client: The Adaptee class has a weird interface. "
          "See, I don't understand it:")
    print(f"Adaptee: {adaptee.specific_request()}", end="\n\n")

    print("Client: But I can work with it via the Adapter:")
    adapter = Adapter()
    client_code(adapter)
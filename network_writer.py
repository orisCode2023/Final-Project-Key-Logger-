import requests
import logging
from interface_writer import IWriter
from Encryption import Crypto
import json

class NetworkWriter(IWriter):
    def __init__(self, url: str, crypto: Crypto):
        self.url = url
        self.crypto = crypto
        logging.basicConfig(level=logging.INFO)

    def send_data(self, encrypted_data: str, machine_name: str) -> None:
        try:
            payload = {
                "machine": machine_name,
                "data": json.dumps(encrypted_data)  # alreading encrypted
            }

            response = requests.post(self.url, json=payload, timeout=10)
            response.raise_for_status()

            logging.info(f"Data successfully sent to {self.url} for machine {machine_name}")

        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to send data to {self.url}: {e}")
        except Exception as e:
            logging.error(f"Unexpected error: {e}")

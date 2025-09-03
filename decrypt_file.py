import sys
import json
from Encryption import Crypto

def xor_decrypt(file_path: str, key: str):
    crypto = Crypto(key)
    with open(file_path, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            encrypted_list = json.loads(line)  # Convert string to list
            decrypted = crypto.process(encrypted_list)
            print("Decrypted:", decrypted)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Usage: python {sys.argv[0]} <file_path> <key>")
        sys.exit(1)

    xor_decrypt(sys.argv[1], sys.argv[2])
class Crypto:
    def __init__(self, key: str):
        self.key_bytes = key.encode('utf-8')

    def process(self, data):

        if isinstance(data, str):
            # encryption
            data_bytes = data.encode('utf-8')
            result = [b ^ self.key_bytes[i % len(self.key_bytes)] for i, b in enumerate(data_bytes)]
        elif isinstance(data, list):
            # decryption
            decrypted_bytes = [b ^ self.key_bytes[i % len(self.key_bytes)] for i, b in enumerate(data)]
            result = bytes(decrypted_bytes).decode('utf-8')
        else:
            raise ValueError("Data must be a string (for encryption) or a list of ints (for decryption).")
        return result


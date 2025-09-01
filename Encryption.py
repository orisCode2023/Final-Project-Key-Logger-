class Crypto:
    def __init__(self, key: str):
        self.key_bytes = key.encode('utf-8')

    def process(self, data):
        """
        פונקציה אחת להצפנה ופענוח:
        - אם data הוא מחרוזת -> מחזירה רשימת מספרים (הצפנה)
        - אם data הוא רשימת מספרים -> מחזירה מחרוזת (פענוח)
        """
        if isinstance(data, str):
            # הצפנה
            data_bytes = data.encode('utf-8')
            result = [b ^ self.key_bytes[i % len(self.key_bytes)] for i, b in enumerate(data_bytes)]
        elif isinstance(data, list):
            # פענוח
            decrypted_bytes = [b ^ self.key_bytes[i % len(self.key_bytes)] for i, b in enumerate(data)]
            result = bytes(decrypted_bytes).decode('utf-8')
        else:
            raise ValueError("Data must be a string (for encryption) or a list of ints (for decryption).")
        return result


# # ===== דוגמה לשימוש =====
# if __name__ == "__main__":
#     key = "mysecret"
#     text = "Hello World!"
#
#     crypto = Crypto(key)
#
#     # הצפנה
#     encrypted = crypto.process(text)
#     print("Encrypted:", encrypted)
#
#     # פענוח
#     decrypted = crypto.process(encrypted)
#     print("Decrypted:", decrypted)

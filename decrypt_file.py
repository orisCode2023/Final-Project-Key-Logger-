
import sys

def xor_decrypt(file_path: str, key: str):
    key_bytes = key.encode("utf-8")

    with open(file_path, "rb") as f:
        data = f.read()

    decrypted_bytes = [b ^ key_bytes[i % len(key_bytes)] for i, b in enumerate(data)]
    result = bytes(decrypted_bytes).decode("utf-8", errors="ignore")
    print(result)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Usage: python {sys.argv[0]} <file_path> <key>")
        sys.exit(1)

    file_path = sys.argv[1]  # הפרמטר הראשון אחרי שם הסקריפט
    key = sys.argv[2]        # הפרמטר השני אחרי שם הסקריפט

    xor_decrypt(file_path, key)

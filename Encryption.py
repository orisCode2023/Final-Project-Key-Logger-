def decrypt_numbers(encrypted_bytes, key):
    """
    מקבלת רשימה של מספרים (בייטים מוצפנים) ומפתח,
    מחזירה את הטקסט המקורי.
    """
    # ממירים את המפתח לבייטים
    key_bytes = key.encode('utf-8')

    # מבצעים XOR שוב על כל מספר עם הבייט המתאים מהמפתח
    decrypted_bytes = [b ^ key_bytes[i % len(key_bytes)] for i, b in enumerate(encrypted_bytes)]

    # ממירים את הרשימה חזרה למחרוזת UTF-8
    return bytes(decrypted_bytes).decode('utf-8')


# ===== שימוש =====
text = []
key = "mysecret"

# קודם הצפנה
def encrypt_numbers(text, key):
    key_bytes = key.encode('utf-8')
    text_bytes = text.encode('utf-8')
    encrypted_bytes = [b ^ key_bytes[i % len(key_bytes)] for i, b in enumerate(text_bytes)]
    return encrypted_bytes

encrypted_numbers = encrypt_numbers(text, key)
# הדפסה
# print("Encrypted numbers:", encrypted_numbers)

# פענוח חזרה
decrypted_text = decrypt_numbers(encrypted_numbers, key)
# הדפסה
# print("Decrypted text:", decrypted_text)


def caesar_encrypt(message, key):
    result = ""
    for char in message:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            result += chr((ord(char) + key - shift) % 26 + shift)
        else:
            result += char
    return result

def caesar_decrypt(encrypted_message, key):
    return caesar_encrypt(encrypted_message, -key)

def main():
    choice = input("Enter 'encrypt' to encrypt or 'decrypt' to decrypt: ").lower()

    if choice == 'encrypt':
        message = input("Enter the message to encrypt: ")
        key = int(input("Enter the key (shift value): "))
        encrypted_message = caesar_encrypt(message, key)
        print("Encrypted message:", encrypted_message)
    elif choice == 'decrypt':
        message = input("Enter the message to decrypt: ")
        key = int(input("Enter the key (shift value): "))
        decrypted_message = caesar_decrypt(message, key)
        print("Decrypted message:", decrypted_message)
    else:
        print("Invalid choice. Please enter 'encrypt' or 'decrypt'.")

if __name__ == "__main__":
    main()

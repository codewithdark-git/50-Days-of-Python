import random

def encode(word):
    if len(word) >= 3:
        first_letter = word[0]
        word = word[1:] + first_letter
        secret_code = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=3)) + word + ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=3))
    else:
        secret_code = word[::-1]
    return secret_code

def decode(secret_code):
    if len(secret_code) < 3:
        decoded_word = secret_code[::-1]
    else:
        secret_code = secret_code[3:-3]
        last_letter = secret_code[-1]
        decoded_word = last_letter + secret_code[:-1]
    return decoded_word

def main():
    choice = input("Enter 'code' to encode or 'decode' to decode: ").lower()

    if choice == 'code':
        message = input("Enter the message to encode: ")
        encoded_message = ' '.join(encode(word) for word in message.split())
        print("Encoded message:", encoded_message)
    elif choice == 'decode':
        message = input("Enter the message to decode: ")
        decoded_message = ' '.join(decode(word) for word in message.split())
        print("Decoded message:", decoded_message)
    else:
        print("Invalid choice. Please enter 'code' or 'decode'.")

if __name__ == "__main__":
    main()

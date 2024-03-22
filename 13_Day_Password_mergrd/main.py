from cryptography.fernet import Fernet

class PasswordManager:
    def __init__(self, key):
        self.key = key
        self.fernet = Fernet(key)
        self.passwords = {}

    def encrypt(self, password):
        encrypted_password = self.fernet.encrypt(password.encode())
        return encrypted_password

    def decrypt(self, encrypted_password):
        decrypted_password = self.fernet.decrypt(encrypted_password).decode()
        return decrypted_password

    def add_password(self, website, username, password):
        encrypted_password = self.encrypt(password)
        self.passwords[website] = {"username": username, "password": encrypted_password}

    def get_password(self, website):
        if website in self.passwords:
            username = self.passwords[website]["username"]
            encrypted_password = self.passwords[website]["password"]
            decrypted_password = self.decrypt(encrypted_password)
            return username, decrypted_password
        else:
            return None

if __name__ == "__main__":
    key = Fernet.generate_key()
    password_manager = PasswordManager(key)

    while True:
        print("Password Manager Menu:")
        print("1. Add Password")
        print("2. Get Password")
        print("3. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            website = input("Enter the website: ")
            username = input("Enter the username: ")
            password = input("Enter the password: ")
            password_manager.add_password(website, username, password)
            print("Password added.")
        elif choice == "2":
            website = input("Enter the website: ")
            result = password_manager.get_password(website)
            if result:
                username, password = result
                print(f"Username: {username}")
                print(f"Password: {password}")
            else:
                print("Password not found.")
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

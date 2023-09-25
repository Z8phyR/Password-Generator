from cryptography.fernet import Fernet


def decrypt_password(cipher_suite):
    try:
        encrypted_password = input("Enter the encrypted password: ")
        decrypted_password = cipher_suite.decrypt(
            encrypted_password.encode()).decode()
        print(f"Decrypted password: {decrypted_password}")
    except ValueError:
        print("Invalid password provided. Please ensure the password is correct and try again.")
    except Exception as e:
        print("An error occurred:", e)


def main():
    try:
        key = input("Enter the encryption key: ").encode('utf-8').strip()
        cipher_suite = Fernet(key)
        decrypt_password(cipher_suite)
    except ValueError as e:
        if "Fernet key must be 32 url-safe base64-encoded bytes" in str(e):
            print("Invalid key provided. Please ensure the key is correct and try again.")
        else:
            print("An error occurred:", e)


if __name__ == '__main__':
    main()

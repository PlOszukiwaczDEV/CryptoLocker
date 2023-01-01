from cryptography.fernet import Fernet
import base64

def write_key(file):
    """
        Write the key
    """
    key = Fernet.generate_key()
    with open(file, "wb") as key_file:
        key_file.write(key)



def load_key(key_file):
    """
        Loads the key
    """
    return open(key_file, "rb").read()

def encrypt(filename, key_file):
    """
    Given a filename (str) and key (bytes), it encrypts the file and write it
    """
    f = Fernet(load_key(key_file))
    with open(filename, "rb") as file:
        # read all file data
        file_data = file.read()
    # encrypt data
    encrypted_data = f.encrypt(file_data)
    # write the encrypted file
    with open(filename, "wb") as file:
        file.write(encrypted_data)

def decrypt(filename, key_file): 
    """
    Given a filename (str) and key (bytes), it decrypts the file and write it
    """
    f = Fernet(load_key(key_file))
    with open(filename, "rb") as file:
        # read the encrypted data
        encrypted_data = file.read()
    # decrypt data
    decrypted_data = f.decrypt(encrypted_data)
    # write the original file
    with open(filename, "wb") as file:
        file.write(decrypted_data)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Cryptolocker by PlOszukiwacz")
    parser.add_argument("-g", "--generate-key", dest="generate_key",
                        help="Generate a new key")
    parser.add_argument("-e", "--encrypt",
                        help="Whether to encrypt the file")
    parser.add_argument("-d", "--decrypt",
                        help="Whether to decrypt the file")
    parser.add_argument("-k", "--key-file", 
                         help="Key to load")

    args = parser.parse_args()
    generate_key = args.generate_key
    key_file = args.key_file

    if generate_key:
        write_key(generate_key)
        print("Key Generated!")
        exit()
    # load the key
    if key_file:
        key = load_key(key_file)

    encrypt_ = args.encrypt
    decrypt_ = args.decrypt

    if encrypt_ and decrypt_:
        print("Please specify whether you want to encrypt the file or decrypt it.")
    elif encrypt_:
        encrypt(encrypt_, key_file)
    elif decrypt_:
        decrypt(decrypt_, key_file)
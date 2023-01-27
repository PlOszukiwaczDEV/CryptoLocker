# imports
from cryptography.fernet import Fernet
import base64
import argparse


def restore(restore_key):
    """
    Restore the key
    """
    with open("restored_key.key", "wb") as f:
        f.write(base64.b85decode(restore_key))
    del restore_key

def write_key(key_file):
    """
    Write the key
    """
    key = Fernet.generate_key()
    with open(key_file, "wb") as f:
        f.write(key)
    # generate the restore key
    restore_key = base64.b85encode(key)
    print("Your restore key:")
    print(str(restore_key, "utf-8"))
    del key
    del restore_key

def load_key(key_file):
    """
    Load the key
    """
    return open(key_file, "rb").read()

def encrypt(file, key_file):
    """
    Encrypt the file
    """
    key = Fernet(load_key(key_file))
    with open(file, "rb") as f:
        file_content = f.read()
    file_content_enc = key.encrypt(file_content)
    with open(file, "wb") as f:
        f.write(file_content_enc)
    del key
    del file_content
    del file_content_enc

def decrypt(file, key_file):
    """
    Decrypt the file
    """
    key = Fernet(load_key(key_file))
    with open(file, "rb") as f:
        file_content = f.read()
    file_content_dec = key.decrypt(file_content)
    with open(file, "wb") as f:
        f.write(file_content_dec)
    del key
    del file_content
    del file_content_dec


if __name__ == "__main__":
    # args
    parser = argparse.ArgumentParser(description="PlOszukiwacz Cryptolocker")
    parser.add_argument("-g", "--generate-key", help="Generate the key")
    parser.add_argument("-k", "--key-file", help="The key file")
    parser.add_argument("-e", "--encrypt", help="File to encrypt")
    parser.add_argument("-d", "--decrypt", help="File to decrypt")
    parser.add_argument("-r", "--restore", help="Restore the key")

    # parse args
    args = parser.parse_args()
    gen_key = args.generate_key
    key_file = args.key_file
    enc = args.encrypt
    dec = args.decrypt
    restore_key = args.restore

    if gen_key: write_key(gen_key)
    elif enc: encrypt(enc, key_file)
    elif dec: decrypt(dec, key_file)
    elif restore_key: restore(restore_key)
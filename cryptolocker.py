from tkinter import *
from tkinter import filedialog
from cryptography.fernet import Fernet
from time import sleep
import os

root = Tk()
root.title('PlOszukiwacz Cryptolocker')
root.geometry("500x750")

# def restore():
#     restore_gui = Tk()
#     restore_gui.title('PlOszukiwacz Cryptolocker')
#     restore_gui.geometry("1000x100")
#     restore_key_label = Entry(restore_gui, font=("Helvetica", 24), bd=0, bg="systembuttonface", width=100)
#     restore_key_label.pack(pady=10, padx=50)
#     restore_key_label.insert(0, "Enter Your Restore Key")
#     restore_yes = Button(restore_gui, text="Restore", font=("Helvetica", 32), command=open("key.key", "wb") as key_file: key_file.write(restore_key_label))
#     restore_yes.pack(pady=50)

def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
        generate_done = Tk()
        generate_done.title('PlOszukiwacz Cryptolocker')
        generate_done.geometry("1000x100")
        generate_done_label = Label(generate_done, text="Generate Done", font=("Helvetica", 20))
        generate_done_label.pack(pady=10)
        # generate_done_label = Label(generate_done, text="Copy This key to safe place: ", font=("Helvetica", 20))
        # generate_done_label.pack(pady=10)
        # restore_key_label = Entry(generate_done, font=("Helvetica", 24), bd=0, bg="systembuttonface", width=100)
        # restore_key_label.pack(pady=10, padx=50)
        # restore_key_label.insert(0, key)


def load_key():
    return open("key.key", "rb").read()

def encrypt():
    filepath = filedialog.askopenfilename(initialdir="/",
                                      title="Open file okay?") #C:\Users\PlOszukiwacz\Desktop\PythonFiles\Cryptolocker
    f = Fernet(load_key())
    with open(filepath, "rb") as file:
        file_data = file.read()
    encrypted_data = f.encrypt(file_data)
    with open(filepath, "wb") as file:
        file.write(encrypted_data)
        encrypt_done = Tk()
        encrypt_done.title('PlOszukiwacz Cryptolocker')
        encrypt_done.geometry("400x100")
        encrypt_done = Label(encrypt_done, text="Encrypt Complited", font=("Helvetica", 20))
        encrypt_done.pack(pady=10)


def decrypt(): 
    f = Fernet(load_key())
    filepath = filedialog.askopenfilename(initialdir="/",
                                          title="Open file okay?")
    with open(filepath, "rb") as file:
        encrypted_data = file.read()
    decrypted_data = f.decrypt(encrypted_data)
    with open(filepath, "wb") as file:
        file.write(decrypted_data)
        decrypt_done = Tk()
        decrypt_done.title('PlOszukiwacz Cryptolocker')
        decrypt_done.geometry("400x100")
        decrypt_done = Label(decrypt_done, text="Decrypt Complited", font=("Helvetica", 20))
        decrypt_done.pack(pady=10)

if __name__ == "__main__":
    # encrypt button
    encrypt_button = Button(root, text="Encrypt", font=("Helvetica", 32), command=encrypt)
    encrypt_button.pack(pady=50)

    #decrypt button
    decrypt_button = Button(root, text="Decrypt", font=("Helvetica", 32), command=decrypt)
    decrypt_button.pack(pady=50)

    # generate key
    generate_button = Button(root, text="Generate Key", font=("Helvetica", 32), command=write_key)
    generate_button.pack(pady=50)

    # restore button
    # restore_button = Button(root, text="Restore key", font=("Helvetica", 32), command=restore)
    # restore_button.pack(pady=50)

    root.mainloop()
    print("Exiting Cryptolocker...")
    sleep(4)
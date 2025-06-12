import tkinter as tk
from tkinter import filedialog, messagebox
from cryptography.fernet import Fernet
import os

# Retrieves existing encryption key or generates a new one if not found
def get_key():
    try:
        with open("secret.key", "rb") as f:
            return f.read()
    except FileNotFoundError:
        key = Fernet.generate_key()
        with open("secret.key", "wb") as f:
            f.write(key)
        return key

# Encrypts the selected file and saves the output with a .enc extension
def encrypt_file():
    file_path = filedialog.askopenfilename()
    if not file_path:
        return
    try:
        with open(file_path, "rb") as f:
            data = f.read()
        encrypted = Fernet(key).encrypt(data)
        with open(file_path + ".enc", "wb") as f:
            f.write(encrypted)
        messagebox.showinfo("Success", f"Encrypted as: {file_path}.enc")
    except Exception as e:
        messagebox.showerror("Error", f"Encryption failed: {e}")

# Decrypts a previously encrypted (.enc) file and outputs with a .dec extension
def decrypt_file():
    file_path = filedialog.askopenfilename(filetypes=[("Encrypted Files", "*.enc")])
    if not file_path:
        return
    try:
        with open(file_path, "rb") as f:
            data = f.read()
        decrypted = Fernet(key).decrypt(data)
        output_path = file_path.replace(".enc", "") + ".dec"
        with open(output_path, "wb") as f:
            f.write(decrypted)
        messagebox.showinfo("Success", f"Decrypted as: {output_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Decryption failed: {e}")

# Initialize the encryption key and configure the application window
key = get_key()
root = tk.Tk()
root.title("File Encryption Tool")
root.geometry("300x180")
root.resizable(False, False)

# GUI layout and control buttons
tk.Label(root, text="File Encryption/Decryption", font=("Arial", 14)).pack(pady=15)
tk.Button(root, text="Encrypt File", width=20, command=encrypt_file).pack(pady=5)
tk.Button(root, text="Decrypt File", width=20, command=decrypt_file).pack(pady=5)
tk.Button(root, text="Exit", width=20, command=root.destroy).pack(pady=10)

# Start the Tkinter event loop
root.mainloop()

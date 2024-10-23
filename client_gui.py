import socket
import os
import tkinter as tk
from tkinter import messagebox, simpledialog
from tqdm import tqdm
from crypto_utils import decrypt_file

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 1024

def connect_and_receive():
    host = simpledialog.askstring("Sunucu IP", "Sunucu IP adresini girin:")
    port = 5001

    if not host:
        messagebox.showwarning("Hata", "IP adresi gerekli!")
        return

    client_socket = socket.socket()
    try:
        client_socket.connect((host, port))
        messagebox.showinfo("Bağlantı", f"{host} adresine bağlanıldı.")
        receive_file(client_socket)
    except Exception as e:
        messagebox.showerror("Bağlantı Hatası", f"Bağlanılamadı: {str(e)}")

def receive_file(client_socket):
    received = client_socket.recv(BUFFER_SIZE).decode()
    filename, filesize, key = received.split(SEPARATOR)
    filesize = int(filesize)

    with open(filename, "wb") as f:
        for _ in tqdm(range(filesize), f"Receiving {filename}", unit="B", unit_scale=True):
            bytes_read = client_socket.recv(BUFFER_SIZE)
            if not bytes_read:
                break
            f.write(bytes_read)

    decrypt_file(filename, key.encode())
    messagebox.showinfo("Başarı", f"{filename.replace('.enc', '')} başarıyla alındı.")
    client_socket.close()

root = tk.Tk()
root.title("Şifreli Dosya İstemcisi")
root.geometry("300x150")

receive_button = tk.Button(root, text="Sunucuya Bağlan ve Dosya Al", command=connect_and_receive)
receive_button.pack(expand=True)

root.mainloop()

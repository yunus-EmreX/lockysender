import socket
import os
import tkinter as tk
from tkinter import filedialog, messagebox
import qrcode
from crypto_utils import generate_key, encrypt_file

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 1024

def start_server():
    host = "0.0.0.0"
    port = 5001

    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen(5)
    messagebox.showinfo("Sunucu", f"Sunucu {port} portunda dinleniyor...")

    ip_address = socket.gethostbyname(socket.gethostname())
    generate_qr(ip_address)

    client_socket, address = server_socket.accept()
    messagebox.showinfo("Bağlantı", f"{address} bağlandı.")

    filename = filedialog.askopenfilename()
    if filename:
        key = generate_key()
        encrypt_file(filename, key)
        send_file(filename + ".enc", key, client_socket)

    client_socket.close()
    server_socket.close()

def generate_qr(ip):
    """IP adresini QR kod olarak gösterir."""
    qr = qrcode.make(ip)
    qr.show()

def send_file(filename, key, client_socket):
    filesize = os.path.getsize(filename)
    client_socket.send(f"{filename}{SEPARATOR}{filesize}{SEPARATOR}{key.decode()}".encode())

    with open(filename, "rb") as f:
        while True:
            bytes_read = f.read(BUFFER_SIZE)
            if not bytes_read:
                break
            client_socket.sendall(bytes_read)

    messagebox.showinfo("Başarı", f"{filename} başarıyla gönderildi.")

root = tk.Tk()
root.title("Şifreli Dosya Sunucusu")
root.geometry("300x150")

start_button = tk.Button(root, text="Sunucuyu Başlat ve Dosya Gönder", command=start_server)
start_button.pack(expand=True)

root.mainloop()

from cryptography.fernet import Fernet

def generate_key():
    """AES şifreleme anahtarı oluşturur."""
    return Fernet.generate_key()

def encrypt_file(file_path, key):
    """Belirtilen dosyayı şifreler."""
    fernet = Fernet(key)
    with open(file_path, 'rb') as f:
        data = f.read()
    encrypted_data = fernet.encrypt(data)
    with open(file_path + ".enc", 'wb') as f:
        f.write(encrypted_data)

def decrypt_file(file_path, key):
    """Şifrelenmiş dosyanın şifresini çözer."""
    fernet = Fernet(key)
    with open(file_path, 'rb') as f:
        encrypted_data = f.read()
    decrypted_data = fernet.decrypt(encrypted_data)
    with open(file_path.replace(".enc", ""), 'wb') as f:
        f.write(decrypted_data)

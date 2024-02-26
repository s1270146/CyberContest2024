import binascii
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend


# バイナリファイルを読み込んで16進数文字列に変換する関数
def binary_to_hex_string(file_path):
    with open(file_path, 'rb') as file:
        binary_data = file.read()
        hex_string = binascii.hexlify(binary_data).decode('utf-8')
    return hex_string

def aes_cbc_decrypt(key, ciphertext):
    cipher = Cipher(algorithms.AES(key), modes.CBC(bytes([0] * 16)), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_text = decryptor.update(ciphertext) + decryptor.finalize()
    return decrypted_text

def hex_to_bytes(hex_string):
    return bytes.fromhex(hex_string)

# 使用例
file_path = 'NoIV.bin'
hex_ciphertext = binary_to_hex_string(file_path)
hex_key = '4285a7a182c286b5aa39609176d99c13'

ciphertext = hex_to_bytes(hex_ciphertext)
key = hex_to_bytes(hex_key)

plaintext = aes_cbc_decrypt(key, ciphertext)

print("Decrypted Text:", plaintext.decode('utf-8'))

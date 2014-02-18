from Crypto import Random
from Crypto.Cipher import AES
import base64
import hashlib

class AESCipher:
    __BLOCK_SIZE = 32

    def __init__(self, key):
        self.__key = hashlib.md5(key.encode()).digest()

    def encrypt(self, raw):
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.__key, AES.MODE_CBC, iv)
        length = AESCipher.__BLOCK_SIZE - len(raw) % AESCipher.__BLOCK_SIZE
        return base64.b64encode(iv + cipher.encrypt(raw + bytes([length]) * length))

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        iv = enc[:16]
        cipher = AES.new(self.__key, AES.MODE_CBC, iv)
        data = cipher.decrypt(enc[16:])
        return data[:-data[-1]]

from Crypto import Random
from Crypto.Cipher import AES
import base64
import hashlib

class AESCipher:
    __BLOCK_SIZE = 32
    __BIN_FLAG = b'\x00'

    def __init__(self, key, b64encode = True):
        self.__key = hashlib.md5(key.encode()).digest()
        self.__b64encode = b64encode

    def encrypt(self, raw):
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.__key, AES.MODE_CBC, iv)
        length = AESCipher.__BLOCK_SIZE - len(raw) % AESCipher.__BLOCK_SIZE
        if type(raw) != bytes:
            raw = bytes(raw, encoding = 'utf-8')
        r = iv + cipher.encrypt(raw + bytes([length]) * length)
        return base64.b64encode(r) if self.__b64encode else AESCipher.__BIN_FLAG + r

    def decrypt(self, enc):
        offset = 0
        if not len(enc):
            raise ValueError("No data given")

        if enc[0] != AESCipher.__BIN_FLAG[0]:
            enc = base64.b64decode(enc)
        else:
            offset = 1
        iv = enc[offset:16+offset]
        cipher = AES.new(self.__key, AES.MODE_CBC, iv)
        data = cipher.decrypt(enc[16+offset:])
        return data[:-data[-1]]

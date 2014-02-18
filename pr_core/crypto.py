from Crypto import Random
from Crypto.Cipher import AES
from struct import pack, unpack
import base64
import hashlib

class AESCipher:
    __BLOCK_SIZE = 32
    __PADDING = '{'
    __pad = lambda s: s + (AESCipher.__BLOCK_SIZE - len(s) % AESCipher.__BLOCK_SIZE) * AESCipher.__PADDING

    __DecodeAES = lambda c, e: str(c.decrypt(e), encoding='utf-8').rstrip(AESCipher.__PADDING)

    def __init__(self, key):
        self.__key = hashlib.md5(key.encode()).digest()

    def encrypt(self, raw):
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.__key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(AESCipher.__pad(raw)))

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        iv = enc[:16]
        cipher = AES.new(self.__key, AES.MODE_CBC, iv)
        return str(cipher.decrypt(enc[16:]), encoding='utf-8').rstrip(AESCipher.__PADDING)

a = AESCipher("Hello")
m = a.encrypt("MEssage")
print(m)
m = a.decrypt(m)
print(m)
exit()
m = a.encrypt(open('__pycache__/__init__.cpython-33.pyc', 'rb').read())
print(m)
m = a.decrypt(m)
open('test', 'wb').write(m)


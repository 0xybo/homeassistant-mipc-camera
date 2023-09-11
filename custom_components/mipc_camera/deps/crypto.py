from binascii import unhexlify, hexlify
from Crypto.Cipher.DES import new as DES, MODE_CBC
from Crypto.Hash.MD5 import new as MD5

def encrypt(password: str, shared_key: str) -> str:
    password = MD5(password.encode()).hexdigest()
    shared_key = MD5(shared_key.encode()).hexdigest()[:16]

    return hexlify(DES(unhexlify(shared_key), MODE_CBC, unhexlify("0000000000000000")).encrypt(unhexlify(password))).decode()

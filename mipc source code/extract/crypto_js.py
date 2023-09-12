from _crypto_js import crypto_js
crypto_js = crypto_js.crypto_js

def encrypt(password:str, shared_key:str) -> str:
    return crypto_js.DES.encrypt(
        crypto_js.MD5(password),
        crypto_js.MD5(shared_key),
        {
            "iv": crypto_js.enc.Hex.parse("0000000000000000"),
            "padding": crypto_js.pad.NoPadding,
        },
    ).ciphertext.toString()
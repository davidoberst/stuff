import base64

key = b"eDWo"

new_plaintext = b'{"showpassword":"yes","bgcolor":"#ffffff"}'

encrypted = b""

for i in range(len(new_plaintext)):
    encrypted += bytes([
        new_plaintext[i] ^ key[i % len(key)]
    ])
    
cookie = base64.b64encode(encrypted)

print(cookie.decode())


#NATAS11 XOR KEY DECRYPT

import base64

#decode base64
encodedCookie = "HmYkBwozJw4WNyAAFyB1VUcqOE1JZjUIBis7ABdmbU1GIjEJAyIxTRg="
decodedC = base64.b64decode(encodedCookie)
#encode XOR
plaintext = b'{"showpassword":"no","bgcolor":"#ffffff"}' #b = bytes
key = b'' #start constructing the key from bytes

for i in range(len(decodedC)):
    key += bytes([decodedC[i] ^ plaintext[i]])

print(key)


import base64
def xor(flag,key):
    f=len(flag)
    cipher=""
    for i in range(0,f):
        cipher += chr(flag[i]^ord(key[i%len(key)]))
    return cipher
flag = 'flag{********************************}'
key = '3c6e0b8a9c15224a8228b9a98ca1531d'
str_2 = 'VQ9XAksAAVYPWgRRC1RSVQ4AAllQDAdYXABZAwJSUgUKUAAABB8='
cipher = base64.b64decode(str_2)
flag = xor(cipher,key)
print(flag)
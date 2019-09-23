import base64
def xor(flag,key):
    f=len(flag)
    k=len(key)
    cipher=""
    for i in range(0,f):
        cipher += chr(ord(flag[i])^ord(key[i%len(key)]))
    return cipher
flag = 'flag{********************************}'
key = '3c6e0b8a9c15224a8228b9a98ca1531d'
cipher = xor(flag,key)
cipher = base64.b64encode(cipher)
print cipher
cipher = base64.b64decode('VQ9XAksAAVYPWgRRC1RSVQ4AAllQDAdYXABZAwJSUgUKUAAABB8=')
print cipher
flag = xor(cipher,key)
print flag

#cipher=VQ9XAksAAVYPWgRRC1RSVQ4AAllQDAdYXABZAwJSUgUKUAAABB8=

#flag=????
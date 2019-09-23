import binascii

data = open("result", "rb").read()

data_2 = open("success_or_not.txt", "w")

for index in data:
    if index == int('0x30', 16):
        data_2.write("0")
    elif index == int('0x31', 16):
        data_2.write("1")

data_2.close()

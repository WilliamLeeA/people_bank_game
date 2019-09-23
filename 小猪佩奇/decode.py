from PIL import Image
import zlib
import binascii
 
data = open('peiqi.png','rb').read()[0x10035:0x1a470]
# data = open('peiqi.png','rb').read()[0x29:0x10031]

# print(len(data))

# print(hex(data[0]))

# print(hex(data[65543]))

zlib_object = zlib.decompressobj()

pre_reslut = zlib_object.decompress(data)

data_result = open("result_3", "wb")
data_result.write(binascii.hexlify(pre_reslut))

data_result.close()

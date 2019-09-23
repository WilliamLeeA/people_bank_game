from PIL import Image
import zlib
import binascii
 
data = open('erweima.png','rb').read()[0x29:0x10c7]
# data = open('peiqi.png','rb').read()[0x29:0x10031]

# print(len(data))

# print(hex(data[0]))

# print(hex(data[65543]))

# zlib_object = zlib.decompressobj()

# pre_reslut = zlib_object.decompress(data)

pre_reslut = zlib.decompress(data)

data_result = open("result_1", "wb")
data_result.write(pre_reslut)

data_result.close()

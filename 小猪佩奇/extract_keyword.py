import binascii

fo = open("test.txt", "r").read()
char = ""
index = 1
start_index = 1
while index != 3876:
    char = char + chr(int(fo[start_index-1:index*8], 2))
    start_index = index*8+1
    index +=1
print(char)

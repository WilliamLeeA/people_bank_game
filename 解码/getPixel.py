from PIL import Image
import binascii

def get_pixel():
    picture = Image.open("xs.png")
    str_text = open("c.txt", "a")
    (width, height) = picture.size
    for y in range(height):
        for x in range(width):
            str_text.write(str(picture.getpixel((x,y))))
        str_text.write("\n")
    str_text.close()

if  __name__ == "__main__":
    get_pixel()
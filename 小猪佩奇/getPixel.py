from PIL import Image
import binascii

def get_pixel():
    picture = Image.open("peiqi.png")
    str_text = open("c.txt", "a")
    str_text_2 = open("d.txt", "a")
    (width, height) = picture.size
    for y in range(height):
        for x in range(width):
            str_text.write(str(picture.getpixel((x,y))))
            if str(picture.getpixel((x,y))) == "(255, 255, 255)":
                str_text_2.write("1")
            elif str(picture.getpixel((x,y))) == "(0, 0, 0)":
                str_text_2.write("0")
        str_text.write("\n")
    str_text.close()

if  __name__ == "__main__":
    get_pixel()
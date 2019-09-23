def do_function():
    str_1 = "gnbi|ebubt`goepffadBoacg`upad21n~"
    index_str = 1
    strtext = open("c.txt", "a")
    for index in str_1:
        if index_str == 1:
            strtext.write(chr((ord(index)-1)) + "")
            index_str -=1
        elif index_str == 0:
            strtext.write(chr((ord(index)-2)) + "")
            index_str +=1

    strtext.close()

if __name__ == "__main__":
    do_function()

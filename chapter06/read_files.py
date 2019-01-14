from os import path
file = path.realpath("chapter06/fb_object.txt")
with open(file, 'r', encoding='utf-16-be') as ins:
    for line in ins:
        print (line)
        break

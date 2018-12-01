from PIL import Image

im = Image.open("images/tower.jpg")

ASCII = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"


width, height = im.size

rsize = round(width / 2), round(height / 2)

print (rsize)

im = im.resize(rsize, Image.ANTIALIAS)

width, height = im.size

pixels = [[0 for x in range (height)] for y in range (width)]

for x in range (0, width):
    for y in range (0, height):
        xy = (x, y)
        pixels[x][y] = im.getpixel(xy)

output = ""

for x in range (0, len(pixels)):
    for y in range (0, len(pixels[x])):
        pixel = pixels[x][y]
        red = pixel[0]
        green = pixel[1]
        blue = pixel[2]

        brightness = (0.2126 * red) + (0.7152 * green) + (0.0722 * blue)

        pixels[x][y] = round(brightness)

        d = 255 / (len(ASCII) - 1)
        brightness = pixels[x][y]

        char_pos = round(brightness / d)

        ascii_char = ASCII[char_pos]
        pixels[x][y] = ascii_char + ascii_char + ascii_char


for y in range (0, height):
    for x in range (0, width):
        output += pixels[x][y]
    output += "\n"

print(output)
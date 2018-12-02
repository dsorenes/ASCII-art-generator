from PIL import Image
import sys

input_image = sys.argv[1]

im = Image.open(input_image)

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

        if (sys.argv[2] == 'lum'):
            brightness = (0.2126 * red) + (0.7152 * green) + (0.0722 * blue)
        elif (sys.argv[2] == 'avg'):
            brightness = (red + green + blue) / 3
        elif (sys.argv[2] == 'minmax'):
            brightness = ((max(red, green, blue)) + min(red, green, blue)) / 2
        else:
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
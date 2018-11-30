from PIL import Image

im = Image.open("tower.jpg")



width, height = im.size

print(width, height)

pixels = [[0 for x in range (height)] for y in range (width)]

for x in range(0, width):
    for y in range (0, height):
        xy = (x, y)
        pixels[x][y] = im.getpixel(xy)



for x in range (0, len(pixels)):
    for y in range (0, len(pixels[x])):
        pixel = pixels[x][y]
        print(pixel)
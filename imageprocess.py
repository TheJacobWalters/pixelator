from PIL import Image
im = Image.open("julia.png")
width, height = im.size
if (width != height):
    if width <= height:
        smaller = width
    else:
        smaller = height

(left, upper, right, lower) = (0, 0, smaller, smaller)
im_crop = im.crop((left, upper, right, lower))
im_crop.show()
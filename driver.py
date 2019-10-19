from PIL import Image
class Pixel:
    def __init__(self):
        self.total_red = 0
        self.total_green = 0
        self.total_blue = 0
        self.numberOfEntries = 0
    def reset (self):
        self.total_red = 0
        self.total_green = 0
        self.total_blue = 0
        self.numberOfEntries = 0
    def incrementAvg(self,pixel):
        self.total_red += pixel[0]
        self.total_green += pixel[1]
        self.total_blue += pixel[2]
        self.numberOfEntries += 1
    def getAverage(self):
        average = []
        average.append(round(self.total_red/self.numberOfEntries))
        average.append(round(self.total_green/self.numberOfEntries))
        average.append(round(self.total_blue/self.numberOfEntries))
        return tuple(average)


class Square:
    def __init__(self, image, pixel, dimension,width, height):
        self.image = image
        self.pixel = pixel
        self.width = width
        self.height = height
        self.dimension = dimension
    
    def colorize (self):
        for w in range(self.dimension):
            for h in range (self.dimension):
                self.pixel.incrementAvg(self.image[w+ self.width,h + self.height])

        for w in range (self.dimension):
            for h in range (self.dimension):
                self.image[w + self.width,h + self.height] = self.pixel.getAverage()

    


pixel_size = 5

im = Image.open("ass.jpg")
width, height = im.size
print("width:{} height:{}".format(width, height))
image = im.load()
pixel = Pixel()


for w in range(0, width, pixel_size):
    for h in range(0, height, pixel_size):
        Square(image, pixel, pixel_size, w, h ).colorize()
        pixel.reset()




im.show()

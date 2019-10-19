from PIL import Image

class Square:
    def __init__(self, image, dimension,width, height):
        self.image = image
        self.width = width
        self.height = height
        self.dimension = dimension
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


    def colorize (self):
        for w in range(self.dimension):
            for h in range (self.dimension):
                self.incrementAvg(self.image[w+ self.width,h + self.height])

        for w in range (self.dimension):
            for h in range (self.dimension):
                self.image[w + self.width,h + self.height] = self.getAverage()


class Image_process:
    def __init__(self, image, width, height, pixel_size):
        self.image = image
        self.width = width
        self.height = height
        self. pixel_size = pixel_size
        for w in range(0, self.width, self.pixel_size):
            for h in range(0, self.height, self.pixel_size):
                Square(self.image, self.pixel_size, w, h ).colorize()
        
pixel_size = 20

im = Image.open("ass.jpg")
width, height = im.size
print("width:{} height:{}".format(width, height))
image = im.load()
Image_process(image, width, height, pixel_size)









im.show()

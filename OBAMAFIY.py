from Myro import *

black = (0, 51, 76)
red = (217, 26, 33)
blue = (112, 150, 158)
yellow = (252, 227, 166)


pic = makePicture(pickAFile())


for pixel in getPixels(pic):
        gray = getBlue(pixel)
        if gray > 182:
           setColor(pixel, yellow)
        elif gray > 120:
           setColor(pixel, blue)
        elif gray > 60:
           setColor(pixel, red)
        elif gray < 60:
           setRGB(pixel, blue)
        
#obamicon(pic)
show(pic)
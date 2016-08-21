#Hw6
#Mark Babatunde
#Section C

from Myro import *
init()

hR = makePicture("horizontalred.png")
vR = makePicture("verticalred.png")
hB = makePicture("horizontalblue.png")
vB = makePicture("verticalblue.png")

def orientationLine(pic):
    height = getHeight(pic)
    width = getWidth(pic)
    
    for x in range(width):
            pix = getPixel(pic, 300, 105)
            r = getRed(pix)
            g = getGreen(pix)
            b = getBlue(pix)
            if r == 255 and g == 255 and b == 255:
                rotate(-1, 5)
                rotate(1, 5)
                colorLine(pic)
                break
            else:
                forward(1, 5)
                backward(1, 5)
                colorLine(pic)
                break
                
def colorLine(pic):
    height = getHeight(pic)
    width = getWidth(pic)
    
    for x in range(width):
            pix = getPixel(pic, 297, 214)
            r = getRed(pix)
            g = getGreen(pix)
            b = getBlue(pix)
            if r == 255 and g == 0 and b == 0:
                beep(1, 800)
                beep(1, 800)
                break
            if r == 0 and g == 0 and b == 255:
                beep(2, 800)
                wait(2)
                beep(2, 800)
                break  

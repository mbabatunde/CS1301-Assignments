#Mark Babatunde and Richard Zhang
#C01
#903158527 / mbabatunde3@gatech.edu
#"I worked on this assignment with Richard Zhang, using only this semester's course materials."

from Myro import *

def GreenScreen():
    pictures=makePicture("GreenScreenbeforeimage2.jpg")
    picture=makePicture("GreenScreenbeforeimage1.jpg")
    for x in range (getWidth(picture)):
        for y in range (getHeight(picture)):
            pixel = getPixel(picture,x,y)
            if getGreen(pixel) > 230 and getRed(pixel) < 20 and getBlue(pixel) < 20:
                setColor(getPixel(picture,x,y),getColor(getPixel(pictures,x,y)))
    show(picture)
#GreenScreen()
    
def SplitScreen():
    pictures=makePicture("SplitScreenBeforeImage1.jpg")
    picture=makePicture("SplitScreenBeforeImage2.jpg")
    for x in range (getWidth(picture)):
        for y in range (getHeight(picture)):
            pixel = getPixel(picture,x,y)
            if getY(pixel) >= (.5)*(getHeight(picture)):
                setColor(getPixel(picture,x,y),getColor(getPixel(pictures,x,y)))    
    show(picture)
#SplitScreen()

def SeeingRed():
    picture = makePicture("Seeing-RedBeforeImage.jpg")
    for x in range (getWidth(picture)):
        for y in range ( getHeight(picture)):
            pixel = getPixel(picture,x,y)
            setRed(pixel, getRed(pixel) + 200)
    show(picture)
#SeeingRed()            
    
pic3 = makePicture("prefade.jpg")

def Fade(pic3):
    picList = []
    ogPic = loadPicture("prefade.jpg")
    ogPic = copyPicture(ogPic)
    fadeTrans = 1
    picNumber = 15
    while picNumber >= 0:
        ogPic = loadPicture("prefade.jpg")
        for i in range(16):
         copy = copyPicture(ogPic)
         for x in getPixels(ogPic):
             red = getRed(x)
             red = red*fadeTrans
             blue = getBlue(x)
             blue = blue*fadeTrans
             green = getGreen(x)
             green = green*fadeTrans
             setRed(x, red)
             setBlue(x, blue)
             setGreen(x, green)
         picList.append(copy)
         fadeTrans = fadeTrans - .1
         picNumber = picNumber - 1
    savePicture(picList,"Faded.gif")
    
#Fade(pic3)
    
pic = makePicture("preoverlay.jpg")
def overlay(pic):
    for x in range(50, 100):
        for y in range(50, 200):
            if x % 2 == 0 and y % 2 == 0:
                pixel = getPixel(pic, x, y)
                setRed(pixel, 255)
                setBlue(pixel, 200)
                setGreen(pixel, 0)

    for x in range(25, 200):
        for y in range(25, 100):
            if x % 2 == 0 and y % 2 == 0:
                pixel = getPixel(pic, x, y)
                setRed(pixel, 0)
                setBlue(pixel, 200)
                setGreen(pixel, 255)
    show(pic)
    savePicture(pic, "overlay.jpg") 
#overlay(pic)

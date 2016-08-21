#Awnish Choudhary, Mark Babatunde, Klest Sula, and Tony Sun 
#Section C1 
#klestsula@gmail.com, awnishc@gmail.com, tony.sun@gatech.edu, markababatunde@gmail.com
#"We worked on the homework assignment alone, using only this semester's course materials." 

from Myro import *

pic3 = makePicture("scene11.png")

#This function fades the final scene of the movie
def Fade(pic3):
    picList = []
    ogPic = loadPicture("scene11.png")
    ogPic = copyPicture(ogPic)
    fadeTrans = 1
    picNumber = 19
    while picNumber >= 0:
        ogPic = loadPicture("scene11.png")
        for i in range(20):
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
         fadeTrans = fadeTrans - .01
         picNumber = picNumber - 1
    savePicture(picList,"fadedscene11.gif")

pic = makePicture("scene3.png")

#tint, tint2, and tint3 all give some type of hue to the picture with Koopa Troopa
#the first tint is red
#the second tint is green
#the third tint is blue
#This tint was created to show it as a warning of an enemy approaching
def tint(pic):
    for x in range(getWidth(pic)):
        for y in range(getHeight(pic)):
            pixel = getPixel(pic, x, y)
            setRed(pixel, 200)
    show(pic)
    savePicture(pic,"redscene3.gif")

def tint2(pic):
    for i in range(getWidth(pic)):
        for j in range(getHeight(pic)):
            pixel = getPixel(pic, i, j)
            setGreen(pixel, 200)
    show(pic)
    savePicture(pic, "greenscene3.gif")

def tint3(pic):
    for a in range(getWidth(pic)):
        for b in range(getHeight(pic)):
            pixel = getPixel(pic, a, b)
            setBlue(pixel, 200)
    show(pic)
    savePicture(pic, "bluescene3.gif")

pic2 = makePicture("scene6-9.jpg")
pic4 = makePicture("heart.jpg")
#This function puts hearts all over the top of the original picture to show that
#Mario has seen his princess and is reunited with her again

def splitScreen():
    pic2 = makePicture("scene7.png")
    pic4 = makePicture("heart.jpg")
    for x in range (getWidth(pic2)):
        for y in range (getHeight(pic2)):
            pixel = getPixel(pic2,x,y)
            if getY(pixel) <= (.3)*(getHeight(pic2)):
                setColor(getPixel(pic2,x,y),getColor(getPixel(pic4,x,y)))
    show(pic2)
    savePicture(pic2, "MarioSeesHisPrincess.jpg")
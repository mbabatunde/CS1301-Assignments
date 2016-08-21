#Mark Babatunde
#Section C1
#"We worked on the homework assignment alone, using only this semester's course materials." 

from Myro import *

def performance():
    one = loadPictures("scene1.gif")
    two = loadPictures("scene2.gif")
    three = loadPictures("redscene3.gif")
    four = loadPictures("greenscene3.gif")
    five = loadPictures("bluescene3.gif")
    six = loadPictures("scene4.gif")
    seven = loadPictures("scene5.gif")
    eight = loadPictures("scene6.gif")
    nine = makePicture("heart.jpg")
    ten = loadPictures("scene8.gif")
    eleven = loadPictures("scene9.gif")
    twelve = loadPictures("scene10.gif")
    thirteen = loadPictures("fadedscene11.gif")
    mario = []
    mario.extend(one)
    mario.extend(two)
    mario.extend(three)
    mario.extend(four)
    mario.extend(five)
    mario.extend(six)
    mario.extend(seven)
    mario.extend(eight)
    mario.append(nine)
    mario.extend(ten)
    mario.extend(eleven)
    mario.extend(twelve)
    mario.extend(thirteen)
    savePicture(mario,"film.gif")

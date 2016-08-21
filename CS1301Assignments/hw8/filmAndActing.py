#Mark Babatunde
#Section C1
#"We worked on the homework assignment alone, using only this semester's course materials." 

from Myro import *

#Mario is looking for Daisy

def firstAction():
    turnLeft(1, 3)
    turnLeft(0.5, 0.5)
    wait(0.3)
    turnRight(0.5, 1)
    wait(0.3)
    turnLeft(0.5, 1.5)
    wait(0.3)
    turnRight(0.5, 2)
    wait(0.3)
    turnLeft(0.5, 0.95)
    forward(0.5, 5)

def scene1():
    picList = []
    for i in range(3):
        turnLeft(.02)
        picList.append(takePicture())
    for i in range(6):
        turnRight(.02)
        picList.append(takePicture())
    for i in range(3):
        turnLeft(.02)
        picList.append(takePicture())
    for i in range(2):
        backward(.05)
        picList.append(takePicture())
    for i in range(3):
        turnLeft(.02)
        picList.append(takePicture())
    for i in range(6):
        turnRight(.02)
        picList.append(takePicture())
    for i in range(3):
        turnLeft(.02)
        picList.append(takePicture())
    for i in range(30):
        forward(.05)
        picList.append(takePicture())
    for i in range(4):
        turnLeft(.02)
        picList.append(takePicture())
    for i in range(40):
        forward(.05)
        picList.append(takePicture())
    for i in range(2):
        turnRight(.02)
        picList.append(takePicture())
    for i in range(2):
        picList.append(takePicture())
    for i in range(4):
        forward(.05)
        picList.append(takePicture())
    for i in range(2):
        picList.append(takePicture())
    stop()
    savePicture(picList, "scene1.gif")        

def scene2():
    picList = []
    for i in range(30):
        picList.append(takePicture())
    for i in range(8):
        forward(.05)
        picList.append(takePicture())
    stop()
    savePicture(picList, "scene2.gif")
    
def scene3():
    pic = takePicture()
    savePicture(pic,"scene3.png")
    
def scene4():
    picList = []
    for i in range(25):
        forward(.05)
        picList.append(takePicture())
    stop()
    savePicture(picList,"scene4.gif")
    
def scene5():
    picList = []
    for i in range(25):
        picList.append(takePicture())
    stop()
    beep(1,800)
    savePicture(picList,"scene5.gif")        

def scene6():
    picList = []
    for i in range(7):
        forward(.05)
        picList.append(takePicture())
    for i in range(3):
        turnRight(.02)
        picList.append(takePicture())
    stop()
    beep(1,800)
    savePicture(picList,"scene6.gif")
    
def scene7():
    pic = takePicture()
    savePicture(pic,"scene7.png")
    
def scene8():
    picList = []
    for i in range(30):
        forward(.05)
        picList.append(takePicture())
    stop()
    beep(1,800)
    savePicture(picList,"scene8.gif")                 

def scene9():
    picList = []
    for i in range(30):
        turnRight(.02)
        picList.append(takePicture())
    stop()
    beep(1,800)
    savePicture(picList,"scene9.gif")
    
def scene10():
    picList = []
    for i in range(40):
        forward(.05)
        picList.append(takePicture())
    stop()
    beep(1,800)
    savePicture(picList,"scene10.gif")
    
def scene11():
    pic = takePicture()
    savePicture(pic,"scene11.png")                

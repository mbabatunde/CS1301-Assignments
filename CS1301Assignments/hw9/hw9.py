#Hw9
#Section C
#Mark Babatunde
#"I worked on the homework assignment alone, using only this semester's course materials."

def machToFPS(machList):
    x = map(lambda i: i * 1116.4370079, machList)
    for i in range(0, len(machList)):
        print(machList[i], "mach is equivalent to", x[i], "feet per second")

def sqPyramidVolume(baseHeightList, volumeList):
    for i in baseHeightList:
        x = map(lambda (x,y): (x*x*y)//3, baseHeightList)
    correctList = filter(lambda y: y in volumeList, x)
    return (correctList)

def makeChange(changeList):
    d,q,di,n,p = changeList[0] * 100, changeList[1] * 25, changeList[2] * 10, changeList[3] * 5, changeList[4] * 1
    newList = [d,q,di,n,p]
    totalValue = reduce(lambda x,y: x+y, newList)
    return (totalValue)

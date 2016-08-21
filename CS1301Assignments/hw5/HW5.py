#Hw5
#Mark Babatunde
#Section C
#GTID: 903158527
#mbabatunde3@gatech.edu
#"I worked on the homework assignment alone, using only this semester's course materials." 

def onlySixths(integers):  
    sixth = []
    for i in integers:
        if i%6 == 0:
            sixth.append(i)
        if all(i%6 != 0 for i in integers):
            return sixth        
    return sixth

def union(a, b):
    aOriginal = sorted(a)
    bOriginal = sorted(b)
    c = aOriginal + bOriginal
    return list(set(c))
    
def multiplyNums(aList):
    num = 1
    for i in aList:
        if type(i) == int:
            num *= i
        elif type(i) == float:
            num *= i
        elif type(i) == list:
            num *= multiplyNums(i)          
    return(num)

def abbreviator(phrase):
    newStr = ""
    for letter in phrase:
        if letter.isupper() == True:
            newStr = newStr + letter
        if letter == "0" or letter == "1" or letter == "2" or letter == "3" or letter == "4" or letter == "5" or letter == "6" or letter == "7" or letter == "8" or letter == "9":
            newStr = newStr + letter
    print(newStr)             

def parse(oldStr, delimit):
    aList = []
    aDel = ""
    newStr = oldStr + delimit
    for letter in newStr:
        if letter != delimit:
            aDel = aDel + letter
        elif letter == delimit:
            aList.append(aDel)
            aDel = "" 
    return aList

def lightStats():
    from Myro import*
    
    x = getLight("left")
    y = getLight("center")
    z = getLight("right")
    
    
    print("Left:", getLight("left"))
    print("Center:", getLight("center"))
    print("Right:", getLight("right"))
    
    aList = [x, y, z]
    
    for i in aList:
        average = sum(aList) / float(len(aList))
        median = sorted(aList)[len(aList)//2]
        value = max(aList) - min(aList)
        newList = [average, median, value]
    return newList
#Hw1
#Mark Babatunde
#Section C
#GTID: 903158527
#mbabatunde3@gatech.edu
#"I worked on the homework assignment alone, using only this semester's course materials."

def machToFPS():
    mach = input("Enter the speed in mach:")
    machfloat = float(mach)
    machconvert = (machfloat * 1116.4370079)
    print (machconvert, "feet/second")
    
def sqPyramidVolume():
    length = input("Enter the length of the base in inches:")
    lengthint = int(length)
    height = input ("Enter the height of the pyramid in inches:")
    heightint = int(height)
    volume = ((lengthint * lengthint * heightint)/3)
    print ("Volume of the square pyramid is", volume, "inches-cubed")    

def makeChange():
    cents = input ("Enter the number of cents:")
    total = int(cents)
    dollars = total // 100
    total = total % 100
    quarters = total // 25
    total = total % 25
    dimes = total // 10
    total = total % 10
    nickels = total // 5
    total = total % 5
    pennies = total
    print (dollars, "dollars", quarters, "quarters", dimes, "dimes", nickels, "nickels", pennies, "pennies")

def PPIIndex():
    pounds = float(input("Enter your weight in pounds:"))
    height = float(input("Enter your height in inches:"))
    PPI = ((pounds / height) * 1.125)
    PPIfloat = float(PPI)
    print("Your corrected PPI is {:.1f}".format(PPIfloat))
        
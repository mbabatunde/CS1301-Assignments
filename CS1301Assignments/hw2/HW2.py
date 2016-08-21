def square(base):
    return (base**2)
    
def taylorSwift(numFans):
    minutes = numFans * 3
    hour = minutes // 60
    hourFloat = float(hour)
    remainder = minutes % 60
    remainderFloat = float(remainder)
    time = hourFloat + 9.00
    time2 = remainderFloat
    print("Taylor Swift is done at {:.0f}".format(time),":","{:.0f}".format(time2), "P.M.")

def girlScoutCookies():
    question = input("How Many Boxes Do You Want?")
    questionint = int(question)
    question2 = input("How Much Money Do You Have?")
    question2int = int(question2)
    boxes = questionint * 4
    leftover = boxes - question2int
    print ("You still need $", leftover)
    
def conversionTime(metersPerSecond):
    feetPS = metersPerSecond * 3.28084
    feetPSfloat = float(feetPS)
    milePS = feetPS / 5280
    mph = milePS * 3600
    mphFloat = float(mph)
    kmPS = metersPerSecond / 1000
    kmh = kmPS * 3600
    kmhFloat = float(kmh)
    print ("You have {:.2f}".format(mphFloat), "mph,", "{:.2f}".format(feetPSfloat), "feet per second,", "and", "{:.2f}".format(kmhFloat), "kilometers per hour")
    
def tipCalculator():
    from math import *
    bill = input("How much is the bill?")
    billFloat = float(bill)
    tip = input("How much would you like to tip?")
    tipFloat = float(tip)
    coupon = input("If you have any coupons, how much do you have? If not, put $0")
    couponFloat = float(coupon)
    tipCeil = ceil(tipFloat)
    tax = 0.08
    cheapMeal = billFloat - couponFloat
    tipPrice = cheapMeal + tipCeil
    taxPrice = tipPrice * tax
    cost = taxPrice + tipPrice
    text = "${:.2f}".format(cost)
    costStr = str(text)
    return costStr
    
def falafel(falafelBalls, hummus, pitaBread):
    food1 = falafelBalls // 6
    food2 = hummus // 2
    maxSandwiches = min(food1, food2, pitaBread)
    print ("With", falafelBalls, "falafel balls,", pitaBread, "pitas and", hummus, "hummus, you can make a maximum of", maxSandwiches, "falafels")
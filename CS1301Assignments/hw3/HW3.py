#Hw3
#Mark Babatunde
#Section C
#"I worked on the homework assignment with the help of Awnish Choudhary, using this semester's course materials, https://docs.python.org/2/library/stdtypes.html, and https://docs.python.org/2/library/functions.html"

def applyToTech(reading, math, writing):
    reading = int(reading)
    math = int(math)
    writing = int(writing)
    
    total = reading + math + writing
    
    if reading > 800 or math > 800 or writing > 800:
        return "Invalid scores. Try again" 
    if reading >= 680 and reading <= 800 and math >= 690 and math <= 800 and writing >= 650 and writing <= 800 and total >= 2060 and total <= 2400:
        return "Congratulations, you have been admitted to Georgia Tech. Go Jackets!"             
    else:
        return "I am sorry to inform you we cannot offer you admission to Georgia Tech"

def guessAge(age):
    age = str(age)
    tries = 1

    while tries <= 6:
        personAge = input("Guess the age")
        
        if personAge == age:
           print("Great job! It took you", tries, "tries to guess the age")
           break
        
        elif personAge == "QUIT" or personAge == "Quit" or personAge == "quit":
           print ("Don\'t' give up just because things are hard!")
           break    
       
        elif personAge != age:
           print ("Try again. Guess the age")
           tries = tries + 1             
        
    print("Thanks for playing!")

def encryptMessage(secretMsg):
    newStr = ""
    for letter in secretMsg:
       if letter.isupper() == True:  #isupper and islower were found on Python's official website to solve this problem
             letter = letter.lower() + "^"
       elif letter.islower() == True:
             letter = letter
       elif letter == "1":
             letter = "@"
       elif letter == "2":
             letter = "#"
       elif letter == "3":
             letter = "$"
       else:
             letter = "*"
             
       newStr = newStr + letter
    return newStr
            
def numberPyramid(num):
    row1 = print(str(num) * num * 2)
    firstVar = 0
    
    for x in range(num):
        num += -1
        firstVar += 1
        
        print(str(num) * int(num) + "  " * firstVar + str(num) * int(num))
        
def reverseMultiTable(n):
    n = int(n)
    x = n
    for i in reversed(range(1, n+1)): #Reversed was found on Python's official website
        for i in reversed(range(1, n+1)):
            print(x * i, end = "\t")
        x = x - 1
        print()

def enoughFor():
    hopefulGrade = input("What letter-grade would you like to get?(A-D)")
    hopefulGrade = hopefulGrade.upper()
    for letter in hopefulGrade:
        if hopefulGrade == "A":
            hopefulGradeNumber = 90      
        elif hopefulGrade == "B":
            hopefulGradeNumber = 80
        elif hopefulGrade == "C":
            hopefulGradeNumber = 70
        elif hopefulGrade == "D":
            hopefulGradeNumber = 60
        else:
            print("Not valid input grade")
            break
            
    currentGrade = int(input("What's your current grade on the class % (0-100)"))
    final = int(input("How much is the final worth?"))
    
               
    finalGrade = (100 * hopefulGradeNumber - (100 - final) * currentGrade)/final
    
    if finalGrade <= 100 and finalGrade >= 0 and hopefulGrade == "A":
        return 'You need', finalGrade, 'in the final to get a A in the class'
    elif finalGrade <= 100 and finalGrade >= 0 and hopefulGrade == "B":
        return 'You need', finalGrade, 'in the final to get a B in the class'
    elif finalGrade <= 100 and finalGrade >= 0 and hopefulGrade == "C":
        return 'You need', finalGrade, 'in the final to get a C in the class'
    elif finalGrade <= 100 and finalGrade >= 0 and hopefulGrade == "D":
        return 'You need', finalGrade, 'in the final to get a D in the class'
    elif finalGrade > 100:
        return "I\'m sorry it\'s impossible for you to get this grade"

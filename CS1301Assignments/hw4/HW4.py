#Hw4
#Mark Babatunde
#Section C
#GTID: 903158527
#mbabatunde3@gatech.edu
#"I worked on the homework assignment alone, using only this semester's course materials." 
from Myro import *

#init("sim")

def signatureAbility():
    for t in timer(15):
        while True:
            beep(3, 800)
            beep(3, 1400)
            beep(3, 2000)
            beep(3, 1700)
            beep(3, 900)
            move(0, 1) # Moves in a circle
            motors(1, 0)
        stop()
    stop()
#signatureAbility()

def secondAbility():
    for t in timer(15):
        while getIR('left') == 1 and getIR('right') == 1:
            forward(1)
        stop()
        turnLeft(2, 1.5) #Avoids objects
        beep(3, 800)
        beep(3, 1400)
        beep(3, 2000)
        beep(3, 1700)
        beep(3, 900)
    stop()
    
#secondAbility()

def thirdAbility():
    #Randomly moves around
    for t in timer(15):
        while True:
            motors(1, 1)
            beep(3, 1500)
            motors(-1, -1)
            beep(3, 2400)
            motors(1, 0)
            beep(3, 3000)
            motors(0, 1)
            beep(3, 1200)
            motors(-1, 0)
            beep(3, 1800)
            motors(0, -1)
            beep(3, 1700)
            motors(-1,1)
            beep(3, 4000)
        stop()
    stop()
#thirdAbility()

def battleMenu():
    superPowers = input("""
                               1. One Ability 
                               2. Two Abilities  
                               3. Three Abilities  
                               4. Exit   
                               Which option would you like?""")
    
    if superPowers == "1":
        while True:
            signatureAbility()
    elif superPowers == "2":
        while True:
            signatureAbility()
            secondAbility()
    elif superPowers == "3":
        while True:
            signatureAbility()
            secondAbility()
            thirdAbility()
    elif superPowers == "4":
        while True:
            print("You have won the battle!")
    else:
            print("I'm sorry, that is not a valid choice.")
            superPowers
 
#battleMenu()   
    
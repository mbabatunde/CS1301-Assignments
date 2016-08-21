#Paired Assignment
#Mark Babatunde
#Section C
#"We worked on the homework assignment together, using this semester's course materials"

from Myro import *

init("sim")

def avoidWalls():
    for t in timer(60):
        while getIR('left') == 1 and getIR('right') == 1:
            forward(1)
        stop()
        turnLeft(2, 1.5)
     stop()   
    
            
beep(1, 800)
beep(1, 1600)
beep(1, 2000)
    
avoidWalls()  

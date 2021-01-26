q1 = 14
q2 = 17.5
q3 =16
q4 =12
q5 =14
L = [q1,q2,q3,q4,q5]
from graphics import *

win = GraphWin('Quiz',700,500)
win.setCoords(-2,-2,12,22)


for i in range(5): 

    box = Rectangle(Point(2*i,1), Point(2*i+2,L[i]))
    box.setFill('brown')
    box.draw(win)
    score = Text(Point(4*i+1,L[i]+0.5),L[i])
    score.setSize(8)
    score.draw(win)    
    
#Horizontal Axis

for i in range(4):
    
    mark = Text(Point(2*i+1,-1) ,str('Quiz '+str(i+1)))
    mark.draw(win)

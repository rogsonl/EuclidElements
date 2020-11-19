from math import nan, tan, radians, sqrt, atan, pi
from Euclid import *
#==============================================================
step=[]
step.append(Point(2,4,"A"))																#0
step.append(Point(4,5,"B"))																#1
step.append(Point(5,4,"C"))						 										#2
step.append(Point(4,2,"D"))																#3
step.append(Line(point1=step[0], point2=step[1], name='Line 1'))				#4
x=atan(step[4].slope)
y=degrees(x)
step.append(Line(point1=step[0],angle=y, name='Line 2'))							#5
step.append(Segment(step[4],2,4,"Segment 1 - same as Segment 2"))				#6
step.append(Segment(step[5],2,4,"Segment 2 - same as Segment 1"))				#7
step.append(Line(point1= step[2], point2=step[3],name="Line3"))				#8
step.append(Intersects(step[4],step[8],"intersect of Line1 and Line3"))		#9
step.append(Circle(step[2],2,"Circle 1"))												#10
step.append(Circle(step[1],2,"Circle 2"))												#11
step.append(Intersects(step[4],step[10]))												#12
step.append(Intersects(step[10],step[11]))											#13


for s in step:
	print(s)
... 
#----------------------------------------------------------

	

#p1=Point(1,1,"Point 1")
#print(Step(p1))
#p2=Point(10,10,"Point 2")
#print(Step(p2))
#c1=Circle(p1,10)
#print(Step(c1))
#l1=Line(p1,45)
#print(Step(l1))
#l2=Line(p1,-45,"Miau")
#print(Step(l2))
#print (Step(Intersects(p1,p2,'Intersect P2P')))
#print(Step(Intersects(p1,l1)))
#print(Step(Intersects(p1,c1)))
#print(Step(Intersects(l1,l2)))
#print(Step(Intersects(c1,l1)))




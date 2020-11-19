from math import nan, tan, sqrt, atan, pi
from enum import Enum


''' Creates a point step identifying the <x,y> coordinates and permits accessing them as p.x and p.y where p=Point class instance'''

RType= Enum(value='ResultType',names=("OnePoint,TwoPoints,NoOverlap,Included,Tangent"),)

T=Turtle
#the following colors come from: http://cng.seas.rochester.edu/CNG/docs/x11color.html which are supposedly usable in python
colors=[	"AliceBlue",
			"AntiqueWhite",
			"Aqua",
			"Aquamarine",
			"Azure",
			"Beige",
			"Bisque",
			"Black",
			"BlanchedAlmond",
			"Blue",
			"BlueViolet",
			"Brown",
			"BurlyWood",
			"CadetBlue",
			"Chartreuse",
			"Chocolate",
			"Coral",
			"CornflowerBlue",
			"Cornsilk",
			"Crimson",
			"Cyan",
			"DarkBlue",
			"DarkCyan",
			"DarkGoldenrod",
			"DarkGray",
			"DarkGreen",
			"DarkKhaki",
			"DarkMagenta",
			"DarkOliveGreen",
			"DarkOrange",
			"DarkOrchid",
			"DarkRed",
			"DarkSalmon",
			"DarkSeaGreen",
			"DarkSlateBlue",
			"DarkSlateGray",
			"DarkTurquoise",
			"DarkViolet",
			"DeepPink",
			"DeepSkyBlue",
			"DimGray",
			"DodgerBlue",
			"FireBrick",
			"FloralWhite",
			"ForestGreen",
			"Fuchsia",
			"Gainsboro",
			"GhostWhite",
			"Gold",
			"Goldenrod",
			"Gray",
			"Green",
			"GreenYellow",
			"Honeydew",
			"HotPink",
			"IndianRed",
			"Indigo",
			"Ivory",
			"jSeaGreen",
			"Khaki",
			"Lavender",
			"LavenderBlush",
			"LawnGreen",
			"LemonChiffon",
			"LightBlue",
			"LightCoral",
			"LightCyan",
			"LightGoldenrodYellow",
			"LightGreen",
			"LightGrey",
			"LightPink",
			"LightSalmon",
			"LightSeaGreen",
			"LightSkyBlue",
			"LightSlateGray",
			"LightSteelBlue",
			"LightYellow",
			"Lime",
			"LimeGreen",
			"Linen",
			"Magenta",
			"Maroon",
			"MediumAquamarine",
			"MediumBlue",
			"MediumOrchid",
			"MediumPurple",
			"MediumSeaGreen",
			"MediumSIateBlue",
			"MediumSpringGreei",
			"MediumTurquoise",
			"MediumVioletRed",
			"MidnightBlue",
			"MintCream",
			"MistyRose",
			"Moccasin",
			"NavajoWhite",
			"Navy",
			"OldLace",
			"Olive",
			"OliveDrab",
			"Orange",
			"OrangeRed",
			"Orchid",
			"PaleGoldenrod",
			"PaleGreen",
			"PaleTurquoise",
			"PaleVioletES]",
			"PapayaWhip",
			"PeachPuff",
			"Peru",
			"Pink",
			"Plum",
			"PowderBlue",
			"Purple",
			"Red",
			"RosyBrown",
			"RoyalBlue",
			"SaddleBrown",
			"Salmon",
			"SandyBrown",
			"Seashell",
			"Sienna",
			"Silver",
			"SkyBlue",
			"SlateBlue",
			"SlateGray",
			"Snow",
			"SpringGreen",
			"SteelBlue",
			"Tan",
			"Teal",
			"Thistle",
			"Tomato",
			"Turquoise",
			"Violet",
			"Wheat",
			"White",
			"WhiteSmoke",
			"Yellow",
			"YellowGreen",
			]
def Formatting(color:str="black",fillcolor:str="white",transparency:int=100,width:int=1):
	''' Set up the color, width of pen, transparency, and all other items necessary to format the object being drawn 

	The color list shows the available color in the system
	'''

def degrees(x:float): #The original degrees in math returns none which is crazy
	return x*180/pi
def radians(x:float):
	return x*pi/180

class Point:
	def __init__(self, x:float,y:float,name:str='Point'):
		self.x=x
		self.y=y
		self.name=name
		self.result=[name,[self.x,self.y]]
		...

	def __eq__(self, value):
		if self.x==value.x and self.y==value.y:
			return True
		else:
			return False

	def __str__(self):
		assert (type(self.x)==type(0.0) or type(self.x)==type(0)) and (type(self.y)==type(0.0) or type(self.y)==type(0)),f"both ordinates({self.x} and {self.y}) must be numbers"
		return  (f"{self.name}, <{self.x}, {self.y}>" )
	__repr__= __str__

	def draw(self):
		up()
		goto(self.x,self.y)
		down()
		write("o")

''' Constants  used in Line.__init__'''
IgnorePoint=Point(0,0)
IgnoreSlope=Ignore=0.0


class Line:
	''' Defines lines, creates segments and draws them
	
	Lines are defined as y intercept slopes and are named, although names are not required.
	Segments are define as point start/end in a dictionary of names. Names are required.
	'''
	def __init__(self,point1:Point,angle:float=IgnoreSlope, point2:Point=IgnorePoint, name='Line'):
		global IgnorePoint, IgnoreSlope
		self.name=name
		if not (angle is IgnoreSlope) and (point2 is IgnorePoint):
			self.slopeIntercept=True
			assert angle<=360.0, f'Angle {angle} are restricted to 0 through 360'
			if angle == 90.0 or angle== 180.0:						#slope exists, but is vertical (infinite)
				self.IsVertical=True
				self.slope=IgnoreSlope				#Allows a check for slope being ignored, keeps it floating.
				self.x0=x
				self.p0=Point(self.x, Ignore)		#line is completely defined by its p0.x component.
			else:
				self.slope=tan(radians(angle))	#Not vertical, slope is the tangent of the angle.
				self.IsVertical=False				#IsVertical is part of the object so it has to be set to false.
				self.x0=0								#Compute the y value for x=0
				self.y0=point1.y-point1.x*self.slope		#p0 = <0,y0> in a slope intercept format.
				self.p0=Point(self.x0,self.y0)
		else:												#We are dealing with 2 point input.
			assert point1!=point2, 'You cannot define a line on a single point.'
			if point2.x==point1.x:					#If the x values of both points are the same, then we have a vertical line
				IsVertical=True						#Flag verticality
				self.slope=IgnoreSlope				#We ignore the slope
				x0=x										#x0 is the x component of any point on the line
				self.p0=Point(x0,Ignore)					#Flags to simply insert into y the y location passed.
			else:
				self.slope= (point2.y-point1.y)/(point2.x-point1.x) #Compute the slope
				self.IsVertical=False				#Specify not vertical
				self.x0=0								#p0.x is always 0 in a slope intercept format
				self.y0=point1.y-point1.x*self.slope
				self.p0=Point(self.x0,self.y0)
		self.result=[name,self.p0,self.slope,self.IsVertical]
		...


	def __str__(self):
		''' Print the formula of the line ''' 
		s=f"{self.name}, slope={self.slope}, Intercept:{self.p0}, IsVertical?={self.IsVertical}"
		return s
	__repr__= __str__
	
	def draw(self,format):
		print("You cannot draw an infinite line, use segment!")
		...


class Segment:
	''' Needed to create this category since segments are what we use in geometry, and compose other objects. '''
	def __init__(self,l:Line,x1:float,x2:float,name:str="Segment",draw:bool=True):
#		''' Return the start and end points of the segment 
#			y1 and y2 are only used when the line is perpendicular.
#		'''
		if l.IsVertical:
			self.p1=Point(self.x0,y1)
			self.p2=Point(self.x0,y2)
			self.result=[name,self.p1,self.p2]
		y1=x1*l.slope + l.p0.y
		y2=x2*l.slope + l.p0.y
		#Compute the length of the segment 
		xS=(x2-x1) **2
		yS=(y2-y1)**2
		lS=xS+yS
		segLen=sqrt(xS + yS)
		self.p1=Point(x1, y1)
		self.p2=Point(x2, y2)
		self.len=segLen
		self.result=[name,self.p1,self.p2]
		if draw:
			self.draw()

	def __str__(self,format:list):
		Formatting (format)
		up()
		goto(p1.x,p1.y)
		down()
		goto(p2.x,p2.y)
		

	def draw(self,color:[]): #haven't decided about how to deal with color so for now, pass parameters to a single function
		up()
		T.goto(x1, y1)
		down()
		T.goto(x2,y2)
		...


class Circle:
	''' Creates a circle step based on the radius and center of the circle: (x-x1)**2 + (y-y1)**2=radius**2'''
	def __init__(self, center:Point, radius:float, name:str='Circle'):
		self.center=center
		self.radius=radius
		self.name=name
		self.result=[self.name,self.center,radius]
		...
		
	def hasPoint(self,p:Point, error:float=0.000001): #Compute r^2=(x-x0)^2+(y-y0)^2
		''' Checks wether p is on the circumference of the circle within e error'''
		left=self.radius**2
		right=(p.x-self.center.x)**2+(p.y-self.center.y)**2
		if abs(left-right)<error:
			return(True)
		else:
			return (False)

	def __str__(self):
		return (f"{self.name}, center={self.center.__str__()},radius={self.radius}" )
	__repr__= __str__

	def draw(self):
		up()
		goto(self.center.x,self.center.y)
		down()
		circle(radius)
		...

class Step:
	''' Each step consists of an optional name, an optional comment, a step number, and a results array from one of the geometric or note classes.  
	
	Steps: 
	A. The Geometric Theorem
	
	The theorem class initiates step counting, and has step 0.  I
		1.	Annotations are associated with the last given step, as needed. When steps are generated, the annotations ae ignored.
		2.	It also means that steps do not change with the addition of annotations. 
	Permitted Types are those recognized in creating steps. Probably more will be defined '''

	PERMITTED_TYPES=[
		"Point2Point", 
		"Point2Line",	 
		"Point2Circle",
		"Line2Line",
		"Line2Circle",
		"Circle2Circle",
		'Theorem',
		"LeftNote",
		"RightNote",
		"AtPoint",
		"Point",
		"Line",
		"LineSegment",
		"Circle",
		]
	id=0
	def __init__(self, object):
		''' Defines a step and adds it to the steps array.
			Each object has its own class, and that type is extracted and compared with the permitted types. Unacceptable classes will cause an interrupt!

			Titles are bold, centered on the top of the page, and repeat every page. They contain a page number and total number of pages in the document. The title object contains a one or more paragraphs of information that overwrite the pixel area.
			
			Left and right text are a a column to the left and right of the pixel screen where geometry is performed.

			AtPoint text is text written at a specific point on the pixel screen.
		'''
		tp=str(type(object))
		try:
			i=tp.index(".")
		except   ValueError:
			print(f"A period was not found in {tp} ")
			exit()
		tp=tp[i+1:-2]
		if tp=="Intersects":
			tp=object.type
		id=0
		gType={"Geometry":["Point","Line","Circle","Point2Point","Point2Line","Point2Circle","Line2Circle","Line2Line","Circle2Circle"], "Text":['Theorem',"LeftNote","RightNote","AtPoint"]}
		...
		if tp in gType["Geometry"]:
			self.type="Geometry"
			self.subType=tp
			Step.id+=1
			self.ID=Step.id
			self.name=object.name
			self.result=object		
		elif tp in gType["Text"]:
			self.type="Text"
			self.subType=tp
			self.name=name
			self.result= object
			self.id=id  #There is no increase to the id since it belongs to the geometric item just written
			...
		else:
			print(f"Did not find an approprite type to process step: {tp}")
			end()
	def __str__(self):
		'''Creates a string used in printing the step, or simply as a definition of the step's components '''
		x=f"type={self.type}, "
		x+=f"subtype={self.subType}, "
		x+=f"id={self.id}, "
		x+=f"name={self.name}, "
		x+=f" result={self.result.__str__()} "
		return x #f"type={self.type}, id={self.id}, name={self.name}, result={self.result.__str__()}"
	__repr__= __str__
	

class Intersects:
	''' Computes the intersects between two geometric figures and returns the self.results in a list. 
	'''
	def pointIntersectPoint(self,p1:Point,p2:Point):
		'''Computes whether 2 points are the same point (intersect) and returns True if the same, false otherwise'''
		if p1.x==p2.x and p1.y==p2.y:		
			self.result.append(OnePoint, p1)
		else:
			self.result.append(TwoPoints,p1,p2)

	def pointIntersectsLine(self,p1:Point,l1:Line):
		y=l1.computeY(p1.x)
		if y!=None:
			self.result.append( p1,True)
		else:
			self.result.append(p1,False)
	def pointIntersectsCircle(self,p1:Point,c1:Circle):
		if c1.hasPoint(p1):
			self.result.append(p1)
			self.result.append(True)
		else: 
			self.result.append(p1)
			self.result.append(False)
		...
	def lineIntersectLine(self,l1:Line,l2:Line):
		''' The slope intercept is slope * x + y0=y 

			So the solution to the intercept is x=(y20-y10)/(slope1-slope2)
			This solution does not work if the slopes are identical (parallel lines)
			If one of the two lines is horizontal and the other is not, the equaion is slope * x + y10 = y20 or x=(y20-y10)/slope1 (l2 assumed horizontal).

			if one of the two lines is vertical and the other is not, the equation is  slope * x + y10 at whatever the x the vertical line is.

			if one of the two lines is vertical and the other horizonal, the intersect is at <x0,y1> 

		'''
		if l1.IsVertical and l2.IsVertical:
			return {"result":[], "name": "both lines are vertical, hence parallel and do not intersect"}
		if l1.slope==l2.slope:
			return {"result":[], "name": "both lines have the same slope, hence  are parallel and do not intersect"}
		x=(l2.p0.y-l1.p0.y)/(l1.slope-l2.slope)
		y=l1.slope*x+l1.p0.y
		y1=l2.slope*x+l2.p0.y
		assert y1==y,"The intercept must be a common point on both lines!"
		return self.result.append(Point(x,y))
		...
	def lineIntersectCircle(self,l1:Line,c1:Circle):
		'''Apply the components of the line and circle to the quadratic equation after using the slope intercept of the line to replace for y
			line: mx+k=y
			circle: r^2=(x-c1.center.x)^2+(y-c1.center.y)^2
		'''
		i=c1.center.x
		j=c1.center.y
		r=c1.radius
		m=l1.slope
		k=l1.p0.y #the y intercept of the line (x=0)
		# Components of the quadratic equation:
		a=m**2+1
		b=-2*i-2*m*j+2*m*k
		c=i**2+j**2+k**2-r**2-2*k*j
		sqr=sqrt(b**2-4*a*c)
		div=2*(m**2+1)
		x1=(-b+sqr)/div
		x2=(-b-sqr)/div
	
		if x1==x2:
			self.result.append(Tangent,x1)  #The result is a point'
		else:
			self.result.append(RType.TwoPoints)
			self.result.append(x1)     
			self.result.append(x2) #The result is 2 points, creating a line segment is a separate process.

	def circleIntersectCircle(self,c1:Circle,c2:Circle):
		'''Computes the points of intersection between 2 circles or informs that there are none.		

		Check out: https://stackoverflow.com/questions/3349125/circle-circle-intersection-points
		Built around python code at : https://gist.github.com/xaedes/974535e71009fa8f090e 
		@summary: calculates intersection points of two circles
		@param circle1: tuple(x,y,radius,name)
		@param circle2: tuple(x,y,radius,name)
		@result: tuple of intersection points (which are (x,y,[name]) tuple)
		'''
		x1,y1,r1=c1.center.x,c1.center.y,c1.radius
		x2,y2,r2=c2.center.x,c2.center.y,c2.radius
		dx,dy = x2-x1,y2-y1
		d = sqrt(dx*dx+dy*dy)
		if d > r1+r2: #The centers are too far apart!
			sef.result.append(NoOverlap)
		if d <= abs(r1-r2):
			self.result.append(Included)
		...
		a = (r1*r1-r2*r2+d*d)/(2*d)
		h = sqrt(r1*r1-a*a)
		xm = x1 + a*dx/d
		ym = y1 + a*dy/d
		xs1 = xm + h*dy/d
		xs2 = xm - h*dy/d
		ys1 = ym - h*dx/d
		ys2 = ym + h*dx/d
		p1=Point(xs1,ys1)
		p2=Point(xs2,ys2)
		
		if p1==p2:
			self.result.append(OnePoint)
			self.result.append(p1)
		else:
			self.result.append(RType.TwoPoints)
			self.result.append(p2)
		assert c1.hasPoint(p1) and c2.hasPoint(p1),"Intersection must be on both circles"

	inter={
			"Point2Point":pointIntersectPoint, 
			"Point2Line":pointIntersectsLine,	 
			"Point2Circle":pointIntersectsCircle,
			"Line2Line":lineIntersectLine,
			"Line2Circle":lineIntersectCircle,
			"Circle2Circle":circleIntersectCircle,	
		 }
	'''Inter is a dictionary of types vs intersections. 
			1.	Point2Point for example means the intersection of 2 points, or that the points co-incide, it returns point or false
			2.	Point2Line means that the point is on the line and returns point or false
			3. Point2Circle means that the point is on the circumference of the circle and returns the point or False
			4. Line2Line means the the lines intersect and returns the intersection point or False.
			5. Lin2Circle means that the lines intersect the circle and returns the 2 intersect points or False
			6. Circle2Circle means that the circles intersect and returns the 2 intersect points or false. 
			The self.result is an array of point of intersection. The type and name is preserved within the object.
	'''

	def __init__(self, ob1, ob2,name='Intersect 2 objects'):

		self.result=[]
		self.name=f"Intersection of {ob1.name}-{ob2.name}"
		self.type=type(ob1).__name__ + "2"+type(ob2).__name__
		if self.type in self.inter:
			self.inter[self.type](self,ob1,ob2)
		else:
			self.type=type(ob2).__name__ + "2" +   type(ob1).__name__
			if self.type in self.inter:
				self.inter [self.type](self,ob2,ob1) 

	def __str__(self):
		result={'result':[],'name':f"{self.name}, {self.type}"}
		x=f"{self.name}, {self.type}, results: "
		for r in self.result:
			if type(r)==Point:
				x+=r.__str__() + " "
			elif type(r)==bool:
				x+=r.__str__() + " "
			elif type(r)==type({}):
				for z in r.items():
					x+= z.__str__()+" "				 
			else:
				x+=str(r) #assumed to be a string since intersections are either point(s) or messages that they did not occur.
				x+=" "
		return  x

	def draw(self):
		for p in self.results:
			...
	__repr__=__str__



		

from turtle import *
screenMinX = -500
screenMinY = -500
screenMaxX = 500
screenMaxY = 500
class Player:
	def _init_(self, name,score,level,money):
		self.name=name
		self.score=score
		self.level=level
		self.money=money
	def print_all(self):
		print(self.name)
		print(self.score)
		print(self.level)
		print(self.money)
	#def Lose_Life(self):
	#	if life = 0
	#		print "You Lose"


#Path:
def Path():
	turtle.penup()
	turtle.hideturtle()
	turtle.speed(0)
	turtle.goto(-925,400)
	turtle.pendown()
	turtle.goto(-550,400)
	turtle.goto(-550,-200)
	turtle.goto(350,-200)
	turtle.goto(350,200)
	turtle.goto(1000,200)
	turtle.penup()
	turtle.goto(-925,325)
	turtle.pendown()
	turtle.goto(-625,325)
	turtle.goto(-625,-275)
	turtle.goto(425,-275)
	turtle.goto(425,125)
	turtle.goto(1000,125)
	turtle.hideturtle()
	
		
class Animal(Turtle):
	def __init__(self,canvas,dx,dy,x, y, health, shape):
		RawTurtle.__init__(self,canvas) #this line keep it as it is
		self.penup()
		self.goto(x,y)
		self.dx=dx
		self.dy=dy
		self.x= x
		self.y= y
		self.health= health
		self.shape(shape)

	def getHealth(self):
		return self.health

	def setHealth(self, x):
		self.health = x

	def Disappearing (self):
		if self.health == 0:
			turtle.hideturtle()

	def Loser_Disappearing (self):
			if x == 100 and y == 100:
				turtle.hideturtle()

	def getRadius(self):
		return 2

	def getdx(self):
		return self.dx

	def getdy(self):
		return self.dy

	def move(self):
	 	x = self.xcor()
	 	y = self.ycor()
	 	x = (self.dx + x - screenMinX) % (screenMaxX - screenMinX) + screenMinX
	 	y = (self.dy + y - screenMinY) % (screenMaxY - screenMinY) + screenMinY
	 	self.goto(x,y)




class Machine(Turtle):
	def __init__(self,x,y,shape,animal,shoot):
		RawTurtle.__init__(self,canvas) #this line keep it as it is
		self.goto(x,y)
		self.shoot=shoot
		self.animal=animal
		self.shape(shape)

class bullets(Turtle):
	def __init__(self,x,y,type,shape):
		RawTurtle.__init__(self,canvas) #this line keep it as it is
		self.goto(x,y)
		self.type=type
		self.shape(shape)
	def getRadius(self):
	    return 2

class Store (Turtle):
	def __init__(self,canvas ,x,y):
		RawTurtle.__init__(self,canvas) #this line keep it as it is
		self.goto(x,y)

#	turtle.penup()
#	turtle.hideturtle()
#	turtle.speed(0)
#	turtle.goto(2000,600)
#	turtle.goto(2250,600)
#	turtle.goto(2250,800)
#	turtle.goto(2000,800)
#	turtle.penup()



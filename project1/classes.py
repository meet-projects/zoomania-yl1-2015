class Player:
	def_init_(self,name,score,level,money)
		self.name=name
		self.score=score
		self.level=level
		self.money=money
	def print_all(self):
		print(self.name)
		print(self.score)
		print(self.level)
		print(self.money)
	def Lose_Life(self):
		if life = 0
			print "You Lose"


#Path:

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
turtle.mainloop()
		
class Animal(turtle):
	def __init__(self, x, y, Type, speed, health)
		self.penup()
		self.goto(x,y)
		self.x= x
		self.y= y
		self.Type= Type
		self.speed= speed
		self.health= health

	def getSize(self):
        return self.size

    def getRadius(self):
        return 2
    
    def getDX(self):
        return self.dx
    
    def getDY(self):
        return self.dy
    
    def setDX(self,dx):
        self.dx = dx
        
    def setDY(self,dy):
        self.dy = dy

	def Disappearing (self):
		if health = 0
			turtle.hideturtle()

	def Loser_Disappearing (self):
			if x = 100 y = 100
				turtle.hideturtle()
	def move(self):
        screen = self.getscreen()
        x = self.xcor()
        y = self.ycor()

        x = (self.dx + x - screenMinX) % (screenMaxX - screenMinX) + screenMinX
        y = (self.dy + y - screenMinY) % (screenMaxY - screenMinY) + screenMinY
        
        self.goto(x,y)

    def intersect(object1,object2):
        dist = math.sqrt((object1.xcor() - object2.xcor())**2 + (object1.ycor() - object2.ycor())**2)
        
        radius1 = object1.getRadius()
        radius2 = object2.getRadius()
        
        # The following if statement could be written as 
        # return dist <= radius1+radius2
        if dist <= radius1+radius2:
            return True
        else:
            return False

class Machine(turtle):
	def __init__(self,x,y,shape,animal,shoot)
		self.goto(x,y)
		self.shoot=shoot
		self.animal=animal
		self.shape(shape)

class bullets(turtle):
	def __init__(self,x,y,type,shape)
		self.goto(x,y)
		self.type=type
		self.shape(shape)
	def getRadius(self):
	    return 2

class Store (turtle):
	def__init__(self,x,y)
		self.goto(x,y)

	turtle.penup():
	turtle.hideturtle()
	turtle.pendown()
	turtle.speed(0)
	turtle.goto(2000,600)
	turtle.goto(2250,600)
	turtle.goto(2250,800)
	turtle.goto(2000,800)
	turtle.penup():



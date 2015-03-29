#This is a demo project for meet Yearlong 2014-15 Y1
from turtle import *
import tkinter.messagebox
import tkinter
import random
import math
from classes import *





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

def main():
    # These 4 lines just to prepare the window of the game, no need to change them
    root = tkinter.Tk()
    root.title("Asteroids!")
    cv = ScrolledCanvas(root,600,600,600,600)
    cv.pack(side = tkinter.LEFT)

    #Here we prepre the new shapes of the game
    t = RawTurtle(cv)
    screen = t.getscreen()
    screen.setworldcoordinates(screenMinX,screenMinY,screenMaxX,screenMaxY)
    screen.register_shape("rock3",((-20, -16),(-21, 0), (-20,18),(0,27),(17,15),(25,0),(16,-15),(0,-21)))
    screen.register_shape("rock2",((-15, -10),(-16, 0), (-13,12),(0,19),(12,10),(20,0),(12,-10),(0,-13)))
    screen.register_shape("rock1",((-10,-5),(-12,0),(-8,8),(0,13),(8,6),(14,0),(12,0),(8,-6),(0,-7)))
    screen.register_shape("ship",((-10,-10),(0,-5),(10,-10),(0,10)))
    screen.register_shape("bullet",((-2,-4),(-2,4),(2,4),(2,-4)))
    screen.register_shape("monkey.gif")
    frame = tkinter.Frame(root)
    frame.pack(side = tkinter.RIGHT,fill=tkinter.BOTH)
    t.ht()
    
    # this function when it is called the game will exit
    def quitHandler():
        root.destroy()
        root.quit()

    #here we are creating the button that you will see it on the right side of the game called Quit
    # the part it says command=quitHandler is telling the button when we click it to run the function quitHandler that we defined above
    quitButton = tkinter.Button(frame, text = "Quit", command=quitHandler)
    quitButton.pack()
    
    screen.tracer(10)
    
    # here we are using the class we defined above to create the spaceShip
    monkey = Animal(cv,1,0,150,0,100, "monkey.gif")
    monkey.getHealth()
    rabbit = Animal(cv,0,0,0,0,150,"circle")
    rabbit.getHealth()
    frog = Animal(cv,0,0,0,-150,200,"triangle")
    frog.getHealth()

    level = 1
    animal_dead = 1 # zero mean all animals dead

    # This is preparing a list that we will store all the astroids in it
    #asteroids = []
    
    # this loop runs 5 times and each time it creates an astroid and adds it to the list of astroids
    #for k in range(5):
        # preparing random variables 
    #    dx = random.random() * 6 - 3 #random speed in x (change in x)
    #    dy = random.random() * 6 - 3 #random speed in y (change in y)
    #    x = random.random() * (screenMaxX - screenMinX) + screenMinX # random starting x location
     #   y = random.random() * (screenMaxY - screenMinY) + screenMinY # random starting y location
     #   size = random.random() * 3 +1 # random size (1 or 2 or 3) since we only defined 3 shapes of astroids

        # here we create the astroid with the random variables we defined above
     #   asteroid = Asteroid(cv,dx,dy,x,y,int(size))

        # here we are adding the astroid to the astroids list
      #  asteroids.append(asteroid)

    # here we a function that we will call it every 5 millisecond (THIS IS WHAT CODE KEEPS RUNNING WHILE THE GAME IS OPEN)
    # this we call it GAME LOOP
    # GAME LOOP (BEGIN)
    def play():
    	monkey.move()
    	#print("hello")
    	#animal_dead = 0
    	#for sadek in asteroids:
    	#	if(sadek.getHealth() > 0):
    	#		animal_dead = animal_dead + sadek.getHealth()
    	#if (animals_dead <= 0):
    	#	level++
    	#monkey.sethealth(100+level*6)
        # Tell all the elements of the game to move
        # Tell the ship to move
        #ship.move()
        # go (loop) though each astroid in the astroids list and tell it to move as well check if it is toucing the ship
        #for sadek in asteroids:
        #    if (intersect(ship,sadek)):
        #        print("You Failed")
        #        quitHandler()
        #    sadek.move()
        # Set the timer to go off again in 5 milliseconds
    	screen.ontimer(play, 5)
    # GAME LOOP (ENDS)

    # Set the timer to go off the first time in 5 milliseconds
    screen.ontimer(play,5)
    # this means call the defined function in class spaceShip turrnLeft for the ship everytime the left arrow key is pushed in the keyboard
    #screen.onkeypress(ship.turnLeft,"Left")
    # this means call the defined function in class spaceShip turrnRight for the ship everytime the right arrow key is pushed in the keyboard
    #screen.onkeypress(ship.turnRight,"Right")
    # this means call the defined function in class spaceShip turrnLeft for the ship everytime the up arrow key is pushed in the keyboard
    #screen.onkeypress(ship.fireEngine,"Up")
    
    screen.listen()
    tkinter.mainloop()
  
if __name__ == "__main__":
    main()
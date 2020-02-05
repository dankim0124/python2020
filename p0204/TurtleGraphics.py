#TurtleGraphics.py
#Name:Dohyun Kim
#Date: 2020-02-04
#Assignment: tutleGraphic

import turtle

def drawSquare(myTurtle, size):
    for i in range(4):
        myTurtle.forward(size)
        myTurtle.right(90)

def drawPolygon (myTurtle, myInt):
    if myInt <3 :
        print ("no polygon with angle less than 3")
        return -1
    angle = 180* (myInt-2)/myInt

    for _ in range(myInt):
        myTurtle.forward(15)
        myTurtle.left(180-angle)
    myTurtle.up()
    myTurtle.forward(100)
    myTurtle.down()
    return 0

def fillCorner(myTurtle, sideIndex):
    for _ in range(4):
        myTurtle.forward(20)
        myTurtle.right(90)

    myTurtle.up()
    tmp = sideIndex * 10- 10
    down ,right  = divmod(tmp, 20)

    print( right, down)
    myTurtle.forward(right)
    myTurtle.right(90)
    myTurtle.forward(10*down)
    myTurtle.left(90)

    myTurtle.fillcolor("Black")
    myTurtle.begin_fill()
    myTurtle.down()

    for _ in range(4):
        myTurtle.forward(10)
        myTurtle.right(90)
    myTurtle.end_fill()

    myTurtle.up()
    myTurtle.forward(30)
    myTurtle.down()

def squaresInSquares(myTurtle, count):

    width = count*10

    for i in range(count):
        for _ in range(4):
            myTurtle.forward(width)
            myTurtle.right(90)

        width = width- 10
        myTurtle.up()
        myTurtle.forward(5)
        myTurtle.right(90)
        myTurtle.forward(5)
        myTurtle.left(90)
        myTurtle.down()

    myTurtle.up()
    #myTurtle.right(90)
    myTurtle.forward(100)
   # myTurtle.left(90)
    myTurtle.down()


def main():

    myTurtle = turtle.Turtle()
    myTurtle.shape("turtle")
    myTurtle.up()

    """
    myTurtle.right(180)
    myTurtle.forward(200)
    myTurtle.right(90)
    myTurtle.forward(200)
    myTurtle.right(90)
"""
    myTurtle.goto(-200,200)
    myTurtle.down()

    drawPolygon(myTurtle, 5) #draws a pentagon
    drawPolygon(myTurtle, 8) #draws an octogon

    myTurtle.up()
    myTurtle.goto(-200, 150)
    myTurtle.down()

    fillCorner(myTurtle, 1)
    fillCorner(myTurtle, 2)
    fillCorner(myTurtle, 3)
    fillCorner(myTurtle, 4) #draws a square with top right corner filled in.

    myTurtle.up()
    myTurtle.goto(-200, 100)
    myTurtle.down()
    squaresInSquares(myTurtle, 5) #draws 5 concentric squares
    squaresInSquares(myTurtle, 3) #draws 3 concentric squares


main()
input("Hit enter to quit") #this keeps the turtle window from disapearing too soon.


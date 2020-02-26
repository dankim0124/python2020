#FunctionExamples.py

import turtle

def drawSquare(myTurtle):
  for i in range(4):
    myTurtle.forward(100)
    myTurtle.right(90)
def drawFlower(myTurtle):
    for i in range(20):
        myTurtle.right(360/20)
        drawSquare(myTurtle)

def main():
  bob = turtle.Turtle()
  drawFlower(bob)

main()

input("Press enter to quit.")
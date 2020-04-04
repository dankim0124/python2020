#Calendar.py

from graphics import *
import datetime

now = datetime.datetime.now()
year = now.year
month = now.month
Box = []
currentDay = 0

#my Func
# big box = 40/70/600/450
# 1 box size : 80/20
# 2 box size : 80,60


# calculate Dates
weekDays = ["Mon","Tues", "Wed", "Thur","Fri", "Sat"," Sun"]
months = ["January","February","March","April","May","June","July","August","September","October","November","December"]

def getFirstMonthDay():
    firstDay=datetime.date(year,month,1).weekday()
    return firstDay


def drawCalander(myWin):
    x1 = 40 # X coordinate for starting point of calendar
    y1 = 70 # Y coordinate for starting point of calendar

    day = 1
    flag =0 # check if it is end of the month.

    # making box for weekdays
    for i in range(7):
        drawBox(myWin, x1, y1, x1+80, y1+20)
        t = Text(Point(x1+40, y1+10 ), weekDays[i])
        t.draw(myWin)
        x1+=80

    # X coordinate for starting point of calendar
    # Y coordinate for starting point of calendar
    x1, y1= 40,90
    for i in range(42):
        drawBox(myWin,x1,y1,x1+80,y1+60)

        if month %2 == 1 and day>31:
            flag = 0

        if (month % 2 == 0 and day > 30) or (month ==2 and day>29):
            flag = 0

        if i == getFirstMonthDay() or flag ==1:
            t = Text(Point(x1 + 40, y1 + 10), day)
            t.draw(myWin)
            Box.append(CalanderBox(day, x1, y1, x1 + 80, y1 + 60,t))
            day+=1
            flag = 1


        if( i %7 ==6):
            x1 = 40
            y1 += 60
        else:
            x1 +=80



class CalanderBox:
    def __init__(self,day,x1,y1,x2,y2,text):
        self.day = day
        self.content  = []
        self.x1 = x1
        self.y1 = y1
        self.x2= x2
        self.y2 = y2
        self.text = text

    def addContent(self,input):
        self.content.append(input)

    def getContent(self):
        return self.content

    def deleteContent(self):
        self.content =[]

#Creating a window
def drawBox(myWin,x1=20,y1=100,x2=50,y2=130):
    """An example function of how to draw a box.
    Also important to see how to pass a window to another function."""
    topLeft = Point(x1, y1)
    bottomRight = Point(x2, y2)
    box = Rectangle(topLeft, bottomRight)
    box.draw(myWin)


def getClick(myWin):
    """This is an example function that will pause the program until the
    user clicks the mouse in the given window. Then the coordinates of
    the click is displayed in the window"""

    clickPoint = myWin.getMouse()

    x = clickPoint.getX()
    y = clickPoint.getY()

    record = 0

    for b in Box:
        if x>=b.x1 and x<=b.x2 and y>=b.y1 and y<=b.y2:

            e = Entry(Point(320,480), 50)
            e.draw(myWin)
            e.setText("Day %i Contents :" % b.day  )
            e.setFill("White")

            myWin.getMouse()
            newContent = e.getText()

            if ( newContent == "delete"):
                b.deleteContent()
                record = 0

            else:
                b.addContent(newContent)
            record = b.day
    getClick2(myWin,e)
    return record


def getClick2(myWin,e):
    clickPoint = myWin.getMouse()
    e.undraw()
    return 0


def drawContent(myWin ,currentDay):
    y = 540
    #i=0

    result = []
    dayText= Text(Point (320,520), "Day : "+ str(currentDay) )
    if Box[currentDay - 1].content != []:
        for c in Box[currentDay-1].content:
            t = Text(Point(320, y), c)
            t.draw(myWin)
            y+=20
            result.append(t)
    return result

def getCalanderString():
   return str(year) + " - " +months[month-1]

def main():
    win = GraphWin("Calendar", 640, 640)
   # getFirstMonthDay()

    # Year & month String
    calanderString = getCalanderString()
    t = Text(Point(320, 10), calanderString)
    t.draw(win)

    drawCalander(win)

    # setting content box
    contents = []
    while(1):

        currentDay = getClick(win)

        if contents != []:
            for i in contents:
                i.undraw()

        for b in Box:
            if b.content != []:
                b.text.setTextColor("Blue")
            else:
                b.text.setTextColor("Black")
        contents = drawContent(win,currentDay)


    input("Press Enter to Quit")
    win.close()

if __name__ == '__main__':
    main()


#Midterm Exam
#Problem1.py
#Name:
#Date:

def listSum(myList):
    """Returns the sum (addition) total of the numbers in the list"""
    result = 0
    for elem in myList:
        result+= elem

    return result


def listAverage(myList):
    """Returns the average value of the numbers in the list"""
    result = 0.0
    for elem in myList:
        result += elem

    result = result / len(myList)
    return result

#Test your new functions in this main
def main():
    testList = [1, 2, 3, 4]
    total = listSum(testList)
    ave = listAverage(testList)

    print("The total of the list is %d and the average is %.2f" %(total, ave))

if __name__ == '__main__':
    main()
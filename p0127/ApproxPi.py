# ApproxPi.py
# Name:
# Date:
# Assignment:
import math
import time

def getPi_sequence(iter, percision ):
    tmp1 = 1;
    tmp2 = 1;
    result =4
    for _ in range(iter):
        tmp1 += 2
        tmp2 *= -1
        result += 4/tmp1*tmp2

    return round(result,percision)

def main():
    realPi = math.pi

    # ask user for decimal percision (up to 10)
    # calculate pi using the approximation technique
    # Loop until the level of percision is reached
    start = time.time()
    percision = int(input( " input percision : "))

    myPi = getPi_sequence(1000,percision)
    print ("Pi : ",myPi)


    end = time.time()
    elapsedTime = end - start
    print("calculated in " , elapsedTime)

main()
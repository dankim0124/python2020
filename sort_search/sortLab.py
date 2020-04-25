# The purpose of this lab is to see the speed of different sorting techniques.
# Use the same random seed to create the same random list of nubmers for each run.
# You can change the number of elements in the arrays
# We will test 3 arrays, one that is already in order, one that is sorted in reverse order, and one that it random.

import time
import random
import os
# Your current working directory needs to see the AllSorts.py
# If you have issues you should comment out this line.
import inline as inline

os.chdir(os.path.dirname(os.path.abspath(__file__)))

import AllSorts
import matplotlib
import matplotlib.pyplot as plt
import numpy as np


def getFigure(result):


    data = result
    X = np.arange(3)
    fig = plt.figure()
    ax = fig.add_axes([0, 0, 1, 1])
    ax.bar(X + 0.00, data[0], color='b', width=0.15)
    ax.bar(X + 0.20, data[1], color='g', width=0.15)
    ax.bar(X + 0.40, data[2], color='r', width=0.15)
    ax.bar(X + 0.60, data[3], color='black', width=0.15)
    ax.bar(X + 0.80, data[4], color='grey', width=0.15)

    plt.show()

funcList = [AllSorts.bubbleSort, AllSorts.bubbleSortEarlyExit, AllSorts.insertionSort, AllSorts.mergeSort, AllSorts.selectionSort]
result =[]
def compare(funcNum,arr1,arr2,arr3):
    global result
    tmp = []
    print("\n\nfunc num : " , funcNum)
    startTime = time.time()
    funcList[funcNum](arr1)
    endTime = time.time()
    elapsedTime = endTime - startTime
    tmp.append(elapsedTime)
    print("Ordered list time: %.5f seconds" % elapsedTime)

    startTime = time.time()
    funcList[funcNum](arr2)
    endTime = time.time()
    elapsedTime = endTime - startTime
    tmp.append(elapsedTime)
    print("Reversed list time: %.5f seconds" % elapsedTime)

    startTime = time.time()
    funcList[funcNum](arr3)
    endTime = time.time()
    elapsedTime = endTime - startTime
    tmp.append(elapsedTime)
    print("Random list time: %.5f seconds" % elapsedTime)

    print("Sorting Complete")
    result.append(tmp)


def main():
    random.seed(2020) # This makes sure that the random list will be the same every time.
    numberTerms = 10000

    orderedList = []
    reversedList = []
    randomList = []

    for i in range(numberTerms):
        orderedList.append(i)
        reversedList.insert(0, i)
        randomList.append(random.randint(1, 10000))

    # Run each of the sorts in different python sessions.
    # The sorts are bubbleSort, bubbleSortEarlyExit, selectionSort, insertionSort, and mergeSort

    print("Begin Sorting %d elements." % numberTerms)
    print ("function Numbers \n 0. Bubble\n 1. Bubble early\n 2. Insertion\n 3. merge \n 4.selection")
    for index in range(5):
        compare(index,orderedList,reversedList,randomList)

        for i in range(numberTerms): #reset list to sort.
            orderedList.append(i)
            reversedList.insert(0, i)
            randomList.append(random.randint(1, 10000))


if __name__ == '__main__':
    main()
    print("result : ",result)
    #result = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
    getFigure(result)
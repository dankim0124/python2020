#NumberTests.py

def isThreeOrFive(n):
    """Returns boolean determination if number is multiple of 3 or 5"""

    if n % 3 == 0 or n % 5 == 0:
        return True
    else:
        return False

def isPrime(p):
    """Returns boolean (True/False) if the value given is prime."""
    for i in range(int(p/2)+1):
        if i <=1 :
            continue
        if p% i ==0:
            return False

    return True

def isEven(n):
    """Returns boolean about given value being even."""

    if n % 2 == 0:
        return True
    else:
        return False

def addNum(numList, num):
    """Adds the given number to the given list. Does not add duplicate values."""
    if num in numList:
        numList.append(num)
    else:
        print ("already in this list.")

def fibonacciSequence(value):
    """Returns a list of numbers in the fibonacci sequence up to the given value"""

    nums = [1, 2]
    size = 2
    n = nums[size - 1] + nums[size - 2]

    while n < value:
        addNum(nums, n)
        size = len(nums)
        n = nums[size - 1] + nums[size - 2]

    return nums

def sumOfList(myList):
    sum = 0
    for i in myList:
        sum += i
    return sum

#Test your new functions in this main
def main():
    knownPrimes = [3, 7, 11, 13, 17]

    num = int(input("Enter a number: "))

    if isPrime(num):
        print("%d is a prime number" %(num))

    if isEven(num):
        print("%d is an even number" %(num))


if __name__ == '__main__':
    main()
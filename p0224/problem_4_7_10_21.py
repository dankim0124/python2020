from NumberTest import *

msg = "{}th Prime num is {}"

def problem4():
    biggest = -1
    result = 0
    tmp_i = -1
    tmp_j =-1
    for i in range(1,100):
        for j in range(1,100):
            tmp = i*j
            tmp1 = tmp
            tmp2 = repr(tmp)[::-1]
            if tmp1 == int(tmp2) and tmp1 >=biggest:
                biggest = tmp1
                tmp_i = i
                tmp_j = j
    print ( tmp_i, " * ",tmp_j ," = ", biggest)
    return biggest


def problem7():
    count = 0
    tmpNum = 2
    while count != 10001:
        if isPrime(tmpNum):
            count += 1
            print(msg.format(count, tmpNum))
        tmpNum += 1

    return tmpNum



def problem10():
    result = []
    count =0
    tmpNum=2
    while tmpNum<100:
        if isPrime(tmpNum):
            result.append(tmpNum)
            count += 1
            print(msg.format(count, tmpNum))
        tmpNum += 1

    return result

#to solve p21
def getDivisor(num):
    result = []
    for i in range(1,int(num/2)+1):
        if num% i ==0:
            result.append(i)

    return result


def problem21():
    sum1 = -2
    sum2 = -1
    result = []
    for i in range(1,10000):
        sum1 = sumOfList(getDivisor(i))
        sum2 = sumOfList(getDivisor(sum1))
        if sum2 == i and i !=sum1:
            result.append( (i,sum1))
    return result

def main():
    print("problem 4 ")
    problem4()
    print("Problem 7\n")
    problem7()
    print("\nProblem 10\n")
    print("sum of list : ", sumOfList(problem10()) , "\n")
    print("\nProblem 21\n")
    print(problem21())



if __name__ == '__main__':
    main()
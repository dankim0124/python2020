#DiceRoll.py
#Name: dohyun kim
#Date: 2020/02/19
#Assignment: dice roll

import random

def main():
    #Create an empty list with possible roll values
    result = [0]*11
    freq = []
    msg = "{0:>4} {1:>4} {2:>4}"
    #Create two dice values ranging from 1 - 6 each
    #find the sum total of the two dice
    iter = 100000
    for i in range(iter):
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        total = die1+die2
        result[total-2]+=1
    #print statictics for dice rolls
    for elem in result:
        freq.append(float(elem)/iter)

    print("num\tcount\tfreq")
    for i in range(len(result)):
        print(msg.format(i+2,result[i],freq[i]))

    print ("RESULT : ", result)

main()
#WordCount.py
#Name:dohyun kim
#Date: 2020/02/19
#Assignment: word Count

# there are some charactor that i can not read in my laptop. so spliting it with regular expression.
# num of chacartor may different.

import re

def main():
    fileName = "gettysberg.txt"
    textFile = open(fileName, 'r')
    countL =0
    countW=0
    countC=0
    for line in textFile:
        countL+=1
        words = re.split('\W+',line)
        for word in words:
            countW+=1
            for letter in word:
                    countC+=1

    print("L:{0:>5}\tW:{1:>5}\tC:{2:>5}".format(countL,countW,countC))

main()
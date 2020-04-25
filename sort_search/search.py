
iter = 0
def binarySearch(myList ,begin,end, num):
	global iter
	iter += 1
	print("mylist : ",myList[begin:end], ",  iter : ", iter)

	if(len(myList[begin:end]) == 0):
		return -1

	mid  = int((begin + end)/2)
	print ( "mid : ", mid )


	if myList[mid] == num :
		return mid
	elif myList[mid] > num:
		return binarySearch(myList,begin,mid-1,num)
	elif myList[mid] <num :
		return binarySearch(myList,mid+1,end,num)

def main():
	myList =[6, 9, 12, 13, 17, 20, 25, 29, 33, 35]
	print( binarySearch(myList,0,len(myList),36))
main()

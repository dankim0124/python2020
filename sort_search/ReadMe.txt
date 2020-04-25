Comparion
	before comparing, I searched each of time complexity.

	1) Bubble sort & Selection sort
		both best and worst case : O(n^2)

	2) merge sort
		best : O(n*Log(n) )
 	3)  Selection sort
		best case (ordered list ) : O(n)
		worst case (reversed list) : O(n^2)

	My code show how much time used in each cases,

		blue bar = bubble sort
		green bar =  bubble early exit
		red bar  = insertion sort
		black bar = merge sort
		gry bar = selection sort
	(and orderedList, reversedList, randomList in order.)

	As it is known selection sort is biggest and merge sort is smallest.
	for example, using merge sort, It takes 0.1 second to sort random list, but it takse 151 seconds using selection sort.

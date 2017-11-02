#bubble_sort.py
def bub_sort(myList):
	moreSwap = True
	while moreSwap:
		moreSwap = False
		for elem in range(len(myList)-1):
			if myList[elem]>myList[elem+1]:
				moreSwap = True
				temp = myList[elem]
				myList[elem] = myList[elem+1]
				myList[elem+1] = temp
		print myList


if __name__ == '__main__':
	l = map(int,raw_input("Enter the elements to be sorted").split(' '))
	bub_sort(l)

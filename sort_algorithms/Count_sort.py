#Count_sort.py

#Works on the principle of sorting data given a large array of repeating numbers

def csort(arr):
	counter = [0]*len(arr)
	for k in arr:
		counter[k]+=1

	ndx = 0
	for i in range(0,len(arr)):
		while(0<counter[i]):
			arr[ndx] = i
			counter[i]-=1
			ndx+=1
			


if __name__=='__main__':
	ar = [2,2,2,2,6,7,8,4,4,4,3,2,9,5,9,6,6]
	csort(ar)
	print ar





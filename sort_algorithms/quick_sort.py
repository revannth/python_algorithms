#quick_sort.py

def quick_sort(A):
	quick_sort2(A,0,len(A)-1)
	

def quick_sort2(A,low,hi):
	if low < hi:
		p = partition(A,low,hi)
		quick_sort2(A,low,p-1)
		quick_sort2(A,p+1,hi)

def partition(A,low,hi):
	pivotIndex = get_pivot(A,low,hi)
	pivotValue = A[pivotIndex]
	A[pivotIndex],A[low] = A[low],A[pivotIndex]
	border = low

	for i in range(low,hi+1):
		if A[i] < pivotValue:
			border+=1
			A[border],A[i] = A[i],A[border]

	A[border],A[low] = A[low],A[border]

	return border

def get_pivot(A, low, hi):
	mid = (hi + low) // 2
	s = sorted([A[low], A[mid], A[hi]])
	if s[1] == A[low]:
		return low
	elif s[1] == A[mid]:
		return mid
	return hi
	

if __name__ == "__main__":
	lis_t= [1,6,4,3,2,9,7,5,0]
	quick_sort(lis_t)
	print lis_t



	


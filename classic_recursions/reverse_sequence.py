#reverse_sequence.py

def rev(lis_t,low,high):
	if low<high-1:
		lis_t[low],lis_t[high-1]=lis_t[high-1],lis_t[low]
		rev(lis_t,low+1,high-1)

if __name__ == '__main__':
	l = [1,2,3,4,5,6]
	rev(l,0,len(l))
	print l
	
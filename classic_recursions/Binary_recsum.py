#Binary_recsum.py

#Binary way of finding the sum of all the elements.
#Time complexity is reduced to half and hence the time complexity is O(n)

def binsum(lis_t,start,stop):
	if start>=stop:
		return 0
	elif start==stop-1:
		return lis_t[start]
	else:
		mid=(start+stop)//2
		return binsum(lis_t,start,mid) + binsum(lis_t,mid+1,stop)

if __name__ == '__main__':
	lis_t = [8,7,65,5,8,4,7,8,3,8]
	print binsum(lis_t,0,len(lis_t)-1)
	

	


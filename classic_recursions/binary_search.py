#binary_search.py

def binsearch(data,target,low,high):
	if low>high:
		return False
	mid = (low+high)//2

	if data[mid]==target:
		return True
	elif data[mid]>target:
		return binsearch(data,target,low,mid-1)
	elif data[mid]<target:
		return binsearch(data,target,mid+1,high)


if __name__ == '__main__':
	li_st=[1,2,3,4,5,5,6,7,8,5,4,3,6,7,203,12]
	li_st.sort()
	print binsearch(li_st,8,0,len(li_st)-1)

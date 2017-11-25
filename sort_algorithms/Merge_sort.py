#Merge_sort.py

#First we define the sort function
def Merge_sort(lis_t,low,high):
	if low<high:
		mid = (low + high)//2
		Merge_sort(lis_t,low,mid)
		Merge_sort(lis_t,mid+1,high)
		Combine(lis_t,low,mid,high)

def Combine(lis_t,low,mid,high):
	temp1 = low
	temp2 = mid+1
	temp_list = []
	while temp1<=mid and temp2<=high:
		if lis_t[temp1]<lis_t[temp2]:
			temp_list.append(int(lis_t[temp1]))
			temp1+=1
		elif lis_t[temp1]>lis_t[temp2]:
			temp_list.append(int(lis_t[temp2]))
			temp2+=1
		elif lis_t[temp1] == lis_t[temp2]:
			temp_list.append(int(lis_t[temp1]))
			temp_list.append(int(lis_t[temp2]))
			temp1+=1
			temp2+=1

	while temp1<=mid:
		temp_list.append(int(lis_t[temp1]))
		temp1+=1
	while temp2<=high:
		temp_list.append(int(lis_t[temp2]))
		temp2+=1
	for i in range(low,high+1):
		lis_t[i] = temp_list[i-low]

	
	

if __name__ =='__main__':
	lis_t= [8,9,30,2,300,5,300,5,18,10]
	Merge_sort(lis_t,0,len(lis_t)-1)
	print(lis_t)


		
	




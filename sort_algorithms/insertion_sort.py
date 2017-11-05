#insertion_sort.py
def ins_sor(lis_t):
	# Traverse through 1 to len(arr)
	for index in range(1,len(lis_t)):
		key = lis_t[index]
		#Move lis_t[0..index-1] greater than key to one position ahead of its current position
		j = index-1
		while j>=0 and key<lis_t[j]:
			lis_t[j+1] = lis_t[j]
			j-=1
		#When the algorithm exits this loop, the position to be inserted has been found and is current position +1
		lis_t[j+1] = key
	return lis_t

if __name__ =='__main__':
	l = [85,30,21,65,81,130,2]
	print ins_sor(l)




#recursive_sum.py

#The time complexity is fine but the space is O(n)

def sumofel(S,n):

	if n==0:
		return S[0]

	else:
		return S[n]+sumofel(S,n-1)


if __name__ == '__main__':

	lis_t = [1,2,3,4,3,5,2]
	print sumofel(lis_t,len(lis_t)-1)


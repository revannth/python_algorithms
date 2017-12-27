#Maximum_Minimum.py


def findmax(L,n):

	if n==1:
		return L[0]
	return maxof(L[n],findmax(L,n-1))


def maxof(A,B):
	if A<B:
		return B
	else:
		return A


if __name__ == '__main__':
	Lis_T = [1,2,5,7,3,6]
	print findmax(Lis_T,len(Lis_T)-1)
	

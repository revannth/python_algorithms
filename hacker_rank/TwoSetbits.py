#TwoSetbits.py
import math
def pw(a,n):
	ans = 1
	m=1000000007
	while(n>0):
		if n&1:
			ans = (ans*a)%m
		a=(a*a)%m
		n=n>>1
	return(ans%m)

if __name__ == '__main__':
	t = int(raw_input())
	for i in range(0,t):
		lsb =1
		j=1
		q=0
		m=1000000007		
		n = int(raw_input())
		j=math.ceil((-1+math.sqrt(1+8*n))/2)
		q = j*(j+1)/2
		msb = pw(2,int(j))
		#print msb
		lsb = pw(2,int(j-1-(q-n)))
		#print lsb
		print (msb+lsb)%m


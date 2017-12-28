#Alternate_power.py


#Uses the logic that x^n of a number is nothing but x*(x^(n//2))^2 for odd and (x^(n//2))^2 for even
#O(n) time complexity


def altpow(x,n):

	if n==0:
		return 1

	else :
		partial = altpow(x,n//2)
		result =  partial*partial
		if n%2==0:
			return result
		else:
			return x*result

if __name__ == '__main__':
	print altpow(2,3)

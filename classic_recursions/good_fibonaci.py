#good_fibonaci.py
def good_fib(n):


	 if n<=1:
	 	return(0,1)

	 else:
	 	(a,b)=good_fib(n-1)
	 return (a+b,a)


if __name__ == '__main__':
	print good_fib(11)

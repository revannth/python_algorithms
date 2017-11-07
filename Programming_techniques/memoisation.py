#memoisation.py

#This is a very useful concept of storing the output of the previously executed recursion and producing it for the next one.
#Basically, to reduce the time overhead, we store use up a little space

#Fibonacci using memoisation
fib_cac = {}

def fib(n):
	#If we have cached the value already then return it
	if n in fib_cac:
		return fib_cac[n]
	#Compute and cache otherwise
	if n==1 or n==2:
		value = 1
	else :
		value = fib(n-1) + fib(n-2)

	#Cache the value in the created dic

	fib_cac[n] = value
	return value

for n in range(1,101):
	print fib(n)
#memoisation_factorial.py

#This is a very useful concept of storing the output of the previously executed recursion and producing it for the next one.
#Basically, to reduce the time overhead, we store use up a little space

#Factorial using memoisation tool

from functools32 import lru_cache



#fact_cac = {}
@lru_cache(maxsize = 500)
def fact(n):

	#if n in fact_cac:
	#	return fact_cac[n]
	if n==1:
		b =  1
	elif n>1:

		 b = n*fact(n-1)
	#fact_cac[n] = b
	return b		 


print fact(50)









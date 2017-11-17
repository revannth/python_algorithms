#Powerfunction.py
from Check_Bit import check_bit

#Writing the power function in O(sizeofdatatype)

def pow(a,n):
	ans = 1
	temp = a
#a raised to the power n
	for i in range(0,10):

		if check_bit(n,i):

			ans*=temp
		#print check_bit(n,i)
		temp*=temp		
	
	print ans	


if __name__ =="__main__" :
	pow(2,8)

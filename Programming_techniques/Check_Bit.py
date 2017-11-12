#Check_Bit.py

#This program checks if a given bit is set for a number

def check_bit(a,i):
	print (a>>i)&1

if __name__ == '__main__':
	check_bit(10,1)
	
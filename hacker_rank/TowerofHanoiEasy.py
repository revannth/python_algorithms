#TowerofHanoiEasy.py
def towh(k):
	if k==1:
		return 1
	else:
		return(2*towh(k-1)+1)

def tow_o_h(k,a,c,temp):
	if k==0:
		return
	else:
		tow_o_h(k-1,a,temp,c)
		print "Move ",k,"from",a,"to",c," "
		tow_o_h(k-1,temp,c,a)

if __name__ == '__main__':
	t = int(raw_input())
	for i in range(0,t):
		b = int(raw_input())
		if b==1:
			print "1"
			print "Move 1 from A to C"
		else:
			print towh(b)
			tow_o_h(b,'A','C','B')


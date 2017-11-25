#Disk_utilization1.py

#This is assuming each directory level to be a number

def Diskutil(pa_th):
	total=pa_th
	if pa_th>1:
		for i in range(1,pa_th):
			total +=Diskutil(pa_th-1)
	return total


if __name__ == '__main__':
	
	print Diskutil(10)
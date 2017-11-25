#Disk_utilization2.py

import os

def disk_util(path):
	total = os.path.getsize(path)
	if os.path.isdir(path):
		for filename in os.listdir(path):
			child = os.path.join(path,filename)
			total+=disk_util(child)
	return total


if __name__ == '__main__':
	print disk_util('/Users/vedalasrinivas/Documents/python_algorithms/'),'bytes'

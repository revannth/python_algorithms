#Mini-Max Sum.py
#!/bin/python
#O(logn+4)



import sys

arr = map(int, raw_input().strip().split(' '))

arr.sort()
n = len(arr)
print "%i %i"%(sum(arr[0:4]),sum(arr[n-4:n]))

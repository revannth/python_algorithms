#Staircase.py
#!/bin/python
#O(n)

import sys


n = int(raw_input().strip())

for i in range(1,n+1):
    print " "*(n-i)+"#"*i

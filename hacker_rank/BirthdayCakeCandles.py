#BirthdayCakeCandles.py
#!/bin/python

import sys

def birthdayCakeCandles(n, ar):
    ar.sort()
    found = False 
    i=n-1
    while not found:
        if ar[i] == ar[i-1] and i>0:
            i = i - 1
            continue
        else:
            found = True
    return i
         

   

n = int(raw_input().strip())
ar = map(int, raw_input().strip().split(' '))
if n==1 or n==0:
    print(n)
else :    
    result = birthdayCakeCandles(n, ar)
    print(n-result)

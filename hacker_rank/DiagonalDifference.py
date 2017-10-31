#DiagonalDifference.py
import sys


n = int(raw_input().strip())
a = []
for a_i in xrange(n):
    a_temp = map(int,raw_input().strip().split(' '))
    a.append(a_temp)
j=0
k=len(a)-1
sum_lower = 0
sum_higher = 0
for lst in a:
    sum_lower += lst[j] 
    j+=1
    sum_higher +=lst[k]
    k-=1
if sum_higher>sum_lower:
    print sum_higher-sum_lower
else:
    print sum_lower-sum_higher
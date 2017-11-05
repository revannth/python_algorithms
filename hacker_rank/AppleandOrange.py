#AppleandOrange.py
#!/bin/python
#O(n)

import sys


s,t = raw_input().strip().split(' ')
s,t = [int(s),int(t)]
a,b = raw_input().strip().split(' ')
a,b = [int(a),int(b)]
m,n = raw_input().strip().split(' ')
m,n = [int(m),int(n)]
apple = map(int,raw_input().strip().split(' '))
orange = map(int,raw_input().strip().split(' '))
a_c = 0
o_c = 0

for item in apple:
    if (a+item)>=s and (a+item)<=t:
        a_c+=1
        
for item in orange:
    if item+b<=t and item+b>=s:
        o_c+=1
        
    
        
    
print a_c 
print o_c
   

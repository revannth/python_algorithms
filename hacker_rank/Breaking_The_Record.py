#Breaking_The_Record.py
#!/bin/python
#0(n)

import sys

def getRecord(s):
    count_h = 0
    count_l = 0
    item_h = s[0]
    item_l = s[0]
    
    for i in range(1,len(s)):
        if s[i]>item_h:
            count_h+=1
            item_h = s[i]
        if s[i]<item_l:
            count_l+=1
            item_l = s[i]
    return count_h,count_l
        
            
            
            
        
           
        
     
        
    

n = int(raw_input().strip())
s = map(int, raw_input().strip().split(' '))
result = getRecord(s)
print " ".join(map(str, result))



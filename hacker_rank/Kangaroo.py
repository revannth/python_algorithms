#Kangaroo.py
#!/bin/python

import sys

def kangaroo(x1, v1, x2, v2):
    # Complete this function
    #Relative Distance Approach
    d_r = x2 - x1
    v_r = v2 - v1
    if v1>v2 and v1!=v2:
        v_r = -v_r
    else:
        return "NO"
        
    t_r = (d_r)//(v_r)
    if x1 + t_r*v1 == x2 + t_r*v2:
        return "YES"
    else:
        return "NO"
       
    
    
   
    

x1, v1, x2, v2 = raw_input().strip().split(' ')
x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]
result = kangaroo(x1, v1, x2, v2)
print(result)

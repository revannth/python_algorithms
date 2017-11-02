#Time_Conversion.py
#!/bin/python

import sys

def timeConversion(s):
    # Complete this function
    b =[]
    t=0
    for x in s[2]:
        if x=='A':
            t=1
            break
        else:
            continue
            
               
        
            
            
    temp = (int(s[0]))
    if temp<12 and t!=1:
        temp+=12
        b.append(temp)
    elif temp == 12 and t==1:
        temp="00"
        b.append(temp)
    else:               
        b.append(s[0])
    
       
    b.append(":")
    b.append(s[1])
    b.append(":")
    for x in s[2]:
        if x=='P' or x=='A':
            break
        else:
            b.append(x)
           

            
   
          
    return b
    

s = map(str,raw_input().split(":"))


result = map(str,timeConversion(s))

str1 = ''.join(str(e) for e in result)
print str1


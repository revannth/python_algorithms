#PlusMinus
#!/bin/python
#O(logn+n/2+n/2)

import sys

def bin_src(l,item):
    found = False
    count,bottom= 0,0
    top = len(l) - 1
    
    while bottom<=top and not found:
        middle = (top + bottom)//2
        if item < l[middle]:
            top = middle -1
        elif item > l[middle]:
            bottom = middle + 1
        elif item == l[middle]:
            found = True
            count = middle
    return count
           
         
               
        

n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))

i_c = 0
n_c = 0
 
arr.sort()
#print arr

term = bin_src(arr,0)
#print term
if arr[term]==0:
    i_c+=1
    for k in arr[term+1:n]:
        if k==0:
            i_c+=1
        elif k>0:
            break
    b = n - (term + i_c) 

    print "%.6f"%(b/(n*1.0))

    for k in arr[0:term]:
        if k==0:
            i_c+=1
            n_c+=1
        elif k<0:
            continue
    #print n_c
    b_c = term - n_c 
    print "%.6f"%(b_c/(n*1.0))
    print "%.6f"%(i_c/(n*1.0))

else:
    for k in arr[0:]:
        if k>0:
            i_c+=1
        elif k<0:
            n_c+=1
    k_n = 0
    print "%.6f"%(i_c/(n*1.0))
    print "%.6f"%(n_c/(n*1.0))
    print "%.6f"%(k_n/(n*1.0))









#comparethetriplets
#O(3)

import sys

def solve(A,B):
    # Complete this function
    count_a,count_b,i=0,0,0
    for i in range(3):
        if A[i]>B[i]:
            count_a+=1
        elif A[i]<B[i]:
            count_b+=1
        else:
            continue
    result = [count_a,count_b]
    return result
    

A =  map(int,raw_input().split())
B =  map(int,raw_input().split())
result = solve(A,B)
print (" ".join(map(str, result)))



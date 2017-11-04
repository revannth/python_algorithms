#GradingStudents.py
O(n)
#!/bin/python

import sys

def solve(grades,num):
    for item in range(n):
        if grades[item]>=38 and grades[item]<=40:
            print 40
               
        elif grades[item]%5>2 and grades[item]>40:
            print "%i"%(grades[item] + 5-grades[item]%5 )
            
        else :
            print grades[item]
            
            
            
    
    

n = int(raw_input().strip())
grades = []
grades_i = 0
for grades_i in xrange(n):
    grades_t = int(raw_input().strip())
    grades.append(grades_t)
result = solve(grades,n)




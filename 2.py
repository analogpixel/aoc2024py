#!/usr/bin/env python

#with open("data/2_demo.txt") as f:
with open("data/2.txt") as f:
    puz = [ tuple(map(int, line.split())) for line in f ] 

def check_safe(l):
    check =   [l[i] - l[i+1] for i in range(len(l) - 1)] 
    if all(n > 0 for n in check) or all(n < 0 for n in check ):
        if (all(abs(n) <=3 for n in check)):
            return True
    return False

def remove_nth(lst,n):
    return lst[:n] + lst[n+1:]

#print( [check_safe(n) for n in puz].count(True) )


# count = 0
# for item in puz:
#     for n in range(0, len(item)):
#         if check_safe( remove_nth(item, n)):
#             count+=1
#             break
#

count = sum(
            any( check_safe(remove_nth(item,n)) for n in range(len(item))) 
            for item in puz
           )

print(count)


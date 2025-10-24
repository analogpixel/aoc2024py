#!/usr/bin/env python

import re

x = []
y = []

for f in open("data/1.txt"):
    m = re.match( r"(\d+)\s+(\d+)",f.strip())
    x.append( int(m.group(1)))
    y.append( int(m.group(2)))

x = sorted(x)
y = sorted(y)
sum = 0
sum2 = 0

for i in range(0, len(x)):
    sum +=  abs( x[i] - y[i] ) 
    sum2 += x[i] * y.count(x[i])
    
print(sum)
print(sum2)

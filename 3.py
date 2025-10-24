#!/usr/bin/env python
import re

#data = open("data/3_demo.txt").read()
data = open("data/3.txt").read()
count=0
for m in re.findall( r"mul\(\d+,\d+\)", data):
    match = re.match( r"mul\((\d+),(\d+)\)", m)
    count += (int(match.group(1)) * int(match.group(2)))

print(count)

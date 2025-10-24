#!/usr/bin/env python
import re

#data = open("data/3_demo_2.txt").read()
data = open("data/3.txt").read()

count=0
for m in re.findall( r"mul\(\d+,\d+\)", data):
    match = re.match( r"mul\((\d+),(\d+)\)", m)
    count += (int(match.group(1)) * int(match.group(2)))

print("Part 1 count:", count)


ldata = list(data)
capture=True
outstring=""

for i in range(0, len(ldata) ):
    if data[i:i+7] == "don't()":
        capture=False
    if data[i:i+4] == "do()":
        capture=True

    if capture:
        outstring += data[i]



count=0
for m in re.findall( r"mul\(\d+,\d+\)", outstring):
    match = re.match( r"mul\((\d+),(\d+)\)", m)
    count += (int(match.group(1)) * int(match.group(2)))

print("Part 2 count:", count)


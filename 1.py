#!/usr/bin/env python
import re

for f in open("data/1_demo.txt"):
    m = re.match( r"(\d+)[ ]+(\d+)",f.strip())
    print(m)

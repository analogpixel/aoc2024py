import itertools

with open("data/7_demo.txt") as f:
    for line in f:
        total , numbers = line.strip().split(':')
        total = int(total)
        numbers = list(map(int, numbers.strip().split(" ")))


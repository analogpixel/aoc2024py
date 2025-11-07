import itertools

with open("data/8_demo.txt") as f:
    puzzle_map = [list(line.strip()) for line in f.readlines()]

a_map = []
for y in range(len(puzzle_map)):
    for x in range(len(puzzle_map[0])):
        if puzzle_map[y][x] == 'A':
            a_map.append( [x,y] )



for c in itertools.combinations( a_map, 2) :
    a , b = c
    j , k = a[0]-b[0], a[1]-b[1]
    print(a,b, j,k)


import itertools

with open("data/8.txt") as f:
    puzzle_map = [list(line.strip()) for line in f.readlines()]

a_map = {}
width = len(puzzle_map[0]) 
height = len(puzzle_map)

for y in range(len(puzzle_map)):
    for x in range(len(puzzle_map[0])):
        key = puzzle_map[y][x]
        if key != ".":
            a_map.setdefault(key, []).append( [x,y] )

antinodes = []

for node_type in a_map:
    for c in itertools.permutations( a_map[node_type] ,2 ) :
        a , b = c
        j , k = a[0]-b[0], a[1]-b[1]

        for z in range(0,80):
            _a = [ a[0]+(j*z) , a[1]+(k*z) ]
            if _a[0] >= 0 and _a[0] < width and _a[1] >=0 and _a[1] < height:
                if not _a in antinodes:
                    antinodes.append(_a)
                    #print(a,b, j,k, _a)

#print(width, height)
#print(antinodes)
print( len(antinodes) )

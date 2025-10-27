#_tmp=[ d.strip() for d in open("data/4_demo.txt").readlines()]
_tmp=[ d.strip() for d in open("data/4.txt").readlines()]
width = len( _tmp[0] )
height = len(_tmp)
data = "".join(_tmp)

def get_direction(x,y, xdir, ydir,count=4):
    global width,height,data
    s=""
    for i in range(0,count):
        if x >=0 and x < width and y >=0 and y < height:
            s += data[x + y*width]
            x += xdir
            y += ydir
    return s

count=0
for x in range(0,width):
    for y in range(0, height):
        for d in [ [0,1], [1,1], [1,0], [1,-1], [0,-1], [-1,-1], [-1,0], [-1,1] ]:
            if get_direction(x,y, d[0], d[1]) == "XMAS":
                count+=1

print("Part 1:", count)

count=0
for x in range(0,width):
    for y in range(0, height):
        s1 = get_direction(x-1, y-1, 1,1, 3) 
        s2 = get_direction(x-1, y+1, 1, -1, 3) 
        if s1 == "MAS" or s1 == "SAM":
            if s2 == "MAS" or s2 == "SAM":
                count +=1

print("Part 2:", count)



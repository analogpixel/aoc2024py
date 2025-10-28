filename = "data/6_demo.txt"
filename = "data/6.txt"
_tmp = [x.strip() for x in open(filename).readlines()]
width = len(_tmp[0])
height = len(_tmp)
data = "".join(_tmp)
x = data.find("^") %  width
y = data.find("^") // width 
x_move_dir = 0
y_move_dir = -1

print(x,y,width, height, data)

def get_xy(data,x,y):
    global width,height

    if x >= width or x < 0 or y >= height or y < 0:
        return "0" 
    else:
        return data[x + (y*width)]

positions = [[x,y]]

while True:
    block = get_xy(data, x+x_move_dir,y+y_move_dir)
    if block == "#":
        # rotate 90
        if [x_move_dir,y_move_dir] == [0,-1]:
            x_move_dir = 1
            y_move_dir = 0
        elif [x_move_dir, y_move_dir] == [1,0]:
            x_move_dir = 0
            y_move_dir = 1
        elif [x_move_dir, y_move_dir] == [0,1]:
            x_move_dir = -1
            y_move_dir = 0
        elif [x_move_dir, y_move_dir] == [-1,0]:
            x_move_dir = 0
            y_move_dir = -1
    if block == "0":
        print("Free:", len(positions))
        break
    else:
        x += x_move_dir
        y += y_move_dir
        if not [x,y] in positions:
            positions.append( [x,y] )





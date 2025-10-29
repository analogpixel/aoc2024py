#from numba import jit

#filename = "data/6_demo.txt"
filename = "data/6.txt"
_tmp = [x.strip() for x in open(filename).readlines()]
width = len(_tmp[0])
height = len(_tmp)
data = "".join(_tmp)
x = data.find("^") %  width
y = data.find("^") // width 

#@jit
def get_xy(data,x,y):
    global width,height

    if x >= width or x < 0 or y >= height or y < 0:
        return "0" 
    else:
        return data[x + (y*width)]

#@jit
def walk_map(map_data, start_x, start_y, new_object=False, loop_count=False ):
    global width,height 
    data = list(map_data)
    x = start_x
    y = start_y
    x_move_dir = 0
    y_move_dir = -1
    seen_states = False

    if new_object:
        nx = new_object[0]
        ny = new_object[1]
        pos = nx + ny*width
        data[pos] = "#"
        seen_states = set()

    positions = set()

    while True:

        if new_object:
            state = (x, y, x_move_dir, y_move_dir)
            if state in seen_states:
                return -1
            seen_states.add(state)

        positions.add( (x,y) )

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
            return positions
        else:
            x += x_move_dir
            y += y_move_dir
          
visited_positions = walk_map(data,x,y) 
print( "Part 1:",  len(visited_positions), 41, 4580)

# Part 2 
total = 0
for px, py in visited_positions:
    if (px, py) == (x, y):
        continue
    
    # Create a copy of the data with the new obstacle
    test_data = list(data)
    pos = px + py * width
    test_data[pos] = "#"
    
    # Simulate the guard's movement
    gx, gy = x, y
    gx_dir, gy_dir = 0, -1
    states = set()
    
    while True:
        state = (gx, gy, gx_dir, gy_dir)
        if state in states:
            total += 1
            break
        states.add(state)
        
        # Check if we can move forward
        next_x = gx + gx_dir
        next_y = gy + gy_dir
        
        if next_x < 0 or next_x >= width or next_y < 0 or next_y >= height:
            # Guard exits the area
            break
            
        next_pos = next_x + next_y * width
        if test_data[next_pos] == "#":
            # Hit obstacle, turn right
            if [gx_dir, gy_dir] == [0, -1]:
                gx_dir, gy_dir = 1, 0
            elif [gx_dir, gy_dir] == [1, 0]:
                gx_dir, gy_dir = 0, 1
            elif [gx_dir, gy_dir] == [0, 1]:
                gx_dir, gy_dir = -1, 0
            elif [gx_dir, gy_dir] == [-1, 0]:
                gx_dir, gy_dir = 0, -1
        else:
            # Move forward
            gx, gy = next_x, next_y

print("Part 2:", total, 6, 1480)

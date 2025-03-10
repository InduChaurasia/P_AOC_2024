"""
AOC day6 : https://adventofcode.com/2024/day/6
"""
from utilities import read_file,Year

def room_map():
    """
    Method reads the input file from data dir
    creates a 2D matric for the guard path 
    returns guard path matrix and start position
    """
    room = []
    start = (-1,-1)
    for i,line in enumerate(read_file(Year.y2024,'day6.txt')):
        room.append(list(line))
        if '^' in room[i]:
            start = (i,room[i].index('^'))
    return room, start

def find_loop_or_path(room,start,start_dir):
    """
    Method finds the path travelled by the guard untill guard leaves the room 
    or
    finds if its never ending path (loop)
    return loop flag and traversed path 
    """
    v_paths = []
    r,c= start
    di= start_dir
    is_loop= False
    while r>=0 and r < len(room) and c>=0 and c < len(room[0]):
        if (r,c,dir) in v_paths:
            is_loop= True
            break
        if di=='up':
            while(r>=0 and room[r][c]!='#'):
                path= (r,c,dir)
                v_paths.append(path)
                r -= 1
            if r>=0 and room[r][c]=='#':
                di= 'right'
                r,c= (r+1,c+1)
        elif di=='right':
            while(c<len(room[0]) and room[r][c]!='#'):
                path= (r,c,dir)
                v_paths.append(path)
                c += 1
            if c<len(room[0]) and room[r][c]=='#':
                di= 'down'
                r,c= (r+1,c-1)
        elif di=='down':
            while r<len(room) and room[r][c]!='#':
                path= (r,c,dir)
                v_paths.append(path)
                r += 1
            if r<len(room) and room[r][c]=='#':
                di= 'left'
                r,c= (r-1,c-1)
        elif di=='left':
            while c>=0 and room[r][c]!='#':
                path= (r,c,dir)
                v_paths.append(path)
                c -= 1
            if c>=0 and room[r][c]=='#':
                di= 'up'
                r,c= (r-1,c+1)
    return is_loop,v_paths

def map_triplets_to_pair(triplets):
    """method is used to map row,column,dir triplets to r,c pairs"""
    return {(i,j) for (i,j,_) in triplets}

def find_path():
    """
    Mthod to find the distinct path length traversed by the guard
    """
    room, start = room_map()
    is_loop, path = find_loop_or_path(room,start,'up')
    if not is_loop:
        print(f'path length {len(set(map_triplets_to_pair(path)))}')
    else:
        print('never ending path found')

def find_obstacles():
    """
    Method is used to find number of obstacles 
    that can be placed to create a loop in guard's path
    """
    room,start = room_map()
    is_loop,path = find_loop_or_path(room,start,'up')
    obstacles = 0
    v_path = []
    if not is_loop:
        for r,c,di in path:
            if (r,c)!=start and (r,c) not in v_path:
                if di=='down':
                    start_dir='left'
                    start= (r-1,c)
                elif di=='left':
                    start_dir='up'
                    start= (r,c+1)
                elif di=='up':
                    start_dir='right'
                    start= (r+1,c)
                else:
                    start_dir='down'
                    start= (r,c-1)

                room[r][c]= '#'
                is_loop,_= find_loop_or_path(room, start,start_dir)
                if is_loop:
                    obstacles += 1
                room[r][c]= '.'
                v_path.append((r,c))
    print(f'obstacles {obstacles}')

def main():
    """main"""
    find_path()
    find_obstacles()

if __name__=='__main__':
    main()

"""AOC day15:https://adventofcode.com/2024/day/15"""
from utilities import read_file,Year

def get_map_and_moves():
    map_data, moves = [], ""
    is_map=True
    for line in read_file(Year.y2024,'day15.txt'):
        if not line:
            is_map=False
            continue
        if is_map:
            map_data.append(list(line))
        else:
            moves+=line
    robot_position=next((i, j) for i, row in enumerate(map_data) for j, val in enumerate(row) if val == '@')
    return map_data,moves,robot_position

def double_map():
    map_data,moves,_=get_map_and_moves()
    replace_dict={'@':['@','.'],'.':['.','.'],'#':['#','#'],'O':['[',']']}
    doubled_map=[]
    rows,cols= len(map_data),len(map_data[0])
    for r in range(rows):
        row=[]
        for c in range(cols):
            val=map_data[r][c]
            row.extend(replace_dict.get(val))
        doubled_map.append(row)
    r_pos=(next((i, j)
                for i, row in enumerate(doubled_map)
                for j, val in enumerate(row) if val == '@'))
    return doubled_map,moves,r_pos

def gps_coordinates_sum(map_data):
    return (sum(i * 100 + j
                for i, row in enumerate(map_data)
                for j, val in enumerate(row) if val in ('O', '[')))

def gps_coordinates_for_wh1(direction_map):
    map_data,moves,robot_position=get_map_and_moves()
    for move in moves:
        robot_position = cruise_through_wh1(map_data, direction_map[move], robot_position)
    print(f'GPS coordinates sum for normal map {gps_coordinates_sum(map_data)}')

def cruise_through_wh1(map_data,direction,robot_position):
    r, c = robot_position
    dr, dc = direction
    new_r, new_c = r + dr, c + dc

    if map_data[new_r][new_c] == '.':
        map_data[r][c], map_data[new_r][new_c] = '.', '@'
        return new_r, new_c

    if map_data[new_r][new_c] == 'O':
        while (0 < new_r < len(map_data) - 1 and 0 < new_c < len(map_data[0]) - 1
               and map_data[new_r][new_c] == 'O'):
            new_r, new_c = new_r + dr, new_c + dc

        if map_data[new_r][new_c] == '.':
            map_data[new_r][new_c] = 'O'
            map_data[r][c], map_data[r + dr][c + dc] = '.', '@'
            return r + dr, c + dc

    return robot_position

def gps_coordinates_for_wh2(direction_map):
    map_data, moves, robot_position = double_map()

    for move in moves:
        robot_position = cruise_through_wh2(map_data, direction_map[move], robot_position)

    print(f'GPS coordinates sum for doubled map: {gps_coordinates_sum(map_data)}')

def cruise_through_wh2(map_data,direction,position):
    can_move,to_move=find_moveables(map_data,direction,position)
    if can_move:
        processed=set()
        to_move=sorted(to_move, key=lambda x: (x[0], x[1]))
        (dr,dc)=direction
        step=1 if dr==-1 or dc==-1 else -1
        start=0 if dr==-1 or dc==-1 else len(to_move)-1
        end=len(to_move) if dr==-1 or dc==-1 else -1
        for i in range(start,end,step):
            r,c=to_move[i]
            if (r,c) not in processed:
                map_data[r+dr][c+dc]=map_data[r][c]
                map_data[r][c]='.'
                processed.add((r,c))
        position=(position[0]+dr,position[1]+dc)
    return position

def find_moveables(map_data,direction,position):
    dr,dc=direction
    r,c=position
    new_r,new_c=r+dr,c+dc
    rows,cols=len(map_data),len(map_data[0])

    if new_r<0 or new_r>=rows-1 or new_c<0 or new_c>=cols-1 or map_data[new_r][new_c]=='#':
        return False,[]
    if map_data[new_r][new_c]=='.':
        return True,[position]
    if map_data[new_r][new_c] in (']', '['):
        cc = -1 if map_data[new_r][new_c] == ']' else 1 if dr!=0 else dc
        move_positions = [(new_r, new_c), (new_r, new_c + cc)] if dr!=0 else [(new_r, new_c)]
        
        to_move = [position]
        for pos in move_positions:
            valid, moves = find_moveables(map_data, direction,pos)
            if not valid:
                return False,[]
            to_move.extend(moves)
        return True,to_move
    return False,[]

def main():
    direction_map={'>':(0,1),'<':(0,-1),'^':(-1,0),'v':(1,0)}
    gps_coordinates_for_wh1(direction_map)
    gps_coordinates_for_wh2(direction_map)

if __name__=='__main__':
    main()

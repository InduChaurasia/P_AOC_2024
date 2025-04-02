"""AOC day 21: https://adventofcode.com/2024/day/21"""
from itertools import permutations
import re
from functools import lru_cache
from utilities import read_file, Year

num_pad={'7':(0,0),'8':(0,1),'9':(0,2),'4':(1,0),'5':(1,1),'6':(1,2),
         '1':(2,0),'2':(2,1),'3':(2,2),'NA':(3,0),'0':(3,1),'A':(3,2)}
dir_pad={'NA':(0,0),'^':(0,1),'A':(0,2),'<':(1,0),'v':(1,1),'>':(1,2)}
invalid_start={'A':'<<','^':'<','<':'^','0':'<','7':'vvv','4':'vv','1':'v'}
path_cache={}

def get_input():
    return list(read_file(Year.y2024, 'day21.txt'))

def find_patterns(pattern,start_char):
    wrong_start=invalid_start.get(start_char)
    moves=set(''.join(p) for p in permutations(pattern))
    valid_moves=set()
    for move in moves:
        if not wrong_start or not move.startswith(wrong_start):
            valid_moves.add(move+'A')
    return valid_moves

@lru_cache(None)
def find_paths(start_char,end_char,is_num_pad):
    if start_char==end_char:
        return {'A'}
    key_pad= num_pad if is_num_pad else dir_pad
    start_point,end_point=key_pad[start_char],key_pad[end_char]
    r_diff, c_diff = end_point[0] - start_point[0], end_point[1] - start_point[1]
    row_moves = ('^' if r_diff < 0 else 'v') * abs(r_diff)
    col_moves = ('<' if c_diff < 0 else '>') * abs(c_diff)
    return find_patterns(row_moves + col_moves, start_char)

@lru_cache
def find_shortest_path_length(code,count,is_num_pad):
    if count==0:
        return len(code)
    shortest_path, start_char = 0, 'A'
    for end_char in code:
        paths=find_paths(start_char,end_char,is_num_pad)
        shortest_sub_path = float('inf')
        shortest_sub_path= min(find_shortest_path_length(path,count-1,False) for path in paths)
        shortest_path+=shortest_sub_path
        start_char=end_char
    return shortest_path

def find_complexities(no_of_key_pads):
    regex = re.compile(r'(\d+)')
    complexity=sum(find_shortest_path_length(code,no_of_key_pads,True)*int(regex.search(code).group()) for code in get_input())
    print(f'complexity for {no_of_key_pads} keypads : {complexity}')

def main():
    #1 numeric and 2 directional keypads
    find_complexities(3)
    #1 numeric and 25 directional keypads
    find_complexities(26)

if __name__ == "__main__":
    main()

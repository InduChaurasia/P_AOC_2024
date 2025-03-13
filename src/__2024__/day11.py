"""
AOC day 11: https://adventofcode.com/2024/day/11
"""
from functools import lru_cache
from utilities import read_file,Year

def init_arrangement()->list[int]:
    return  list(map(int, read_file(Year.y2024, 'day11.txt')[0].split()))

def apply_rule(num)->list[int]:
    if num == 0:
        return [1]
    num_str = str(num)
    length = len(num_str)
    if length % 2 == 0:
        mid = length // 2
        return [int(num_str[:mid]), int(num_str[mid:])]
    return [num * 2024]

@lru_cache(None)
def blink(num,bcount)->int:
    if bcount == 0:
        return 1
    return sum(blink(n, bcount - 1) for n in apply_rule(num))

def stone_count(bcount)->None:
    stones = sum(blink(n,bcount) for n in init_arrangement())
    print(f'after {bcount} blinks: {stones}')

def main()->None:
    stone_count(25)
    stone_count(75)

if __name__=='__main__':
    main()

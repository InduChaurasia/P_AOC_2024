"""AOD day 14: https://adventofcode.com/2024/day/14"""
import re
import math
import sys
from utilities import read_file,Year

def robots_details()->tuple[tuple[int,int],tuple[int,int]]:
    pattern = re.compile(r'[-]?\d+')
    robots=[]
    for line in read_file(Year.y2024,'day14.txt'):
        nums = list(map(int, re.findall(pattern, line)))
        robots.append(((nums[1],nums[0]),(nums[3],nums[2])))
    return robots

def print_positions(positions:list[list[int]]):
    for row in positions:
        print(" ".join(map(str, row)))

def robot_positions(robots: list[tuple[tuple[int, int], tuple[int, int]]],after_time:int):
    r,c,=103,101
    mr,mc=r//2,c//2
    positions=[[0] * c for _ in range(r)]
    quater_count=[0,0,0,0]
    for (cr,cc),(vr,vc) in robots:
        dr,dc = cr+vr*after_time, cc+vc*after_time
        fr = r-(dr*-1%r) if dr<0 else dr%r
        fc = c-(dc*-1%c) if dc<0 else dc%c
        fr = 0 if dr<0 and fr==r else fr
        fc = 0 if dc<0 and fc==c else fc

        if fr<mr and fc<mc:
            quater_count[0]+=1
        elif fr<mr and fc>mc:
            quater_count[1]+=1
        elif fr>mr and fc<mc:
            quater_count[2]+=1
        elif fr>mr and fc>mc:
            quater_count[3]+=1

        positions[fr][fc]+= 1

    return positions,quater_count

def safety_factor(robots: list[tuple[tuple[int, int], tuple[int, int]]],after_time:int):
    _,quater_count=robot_positions(robots,after_time)
    return math.prod(quater_count),_

def lowest_safety_factor(robots: list[tuple[tuple[int, int], tuple[int, int]]]):
    min_factor=sys.maxsize
    best_time=None
    best_position=None

    for time in range(100, 10000):
        factor, positions = safety_factor(robots,time)
        if factor < min_factor:
            min_factor, best_time, best_position = factor, time, positions
    print(f'lowest safety factor at time {best_time} : {min_factor}')
    print_positions(best_position)

def main():
    robots=robots_details()
    factor,_=safety_factor(robots,100)
    print(f'safety factor after 100 secons: {factor}')
    lowest_safety_factor(robots)

if __name__=='__main__':
    main()

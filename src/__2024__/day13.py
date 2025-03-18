"""AOC day 13: https://adventofcode.com/2024/day/13"""
import re
from utilities import read_file,Year

def get_machines():
    machines=[]
    pattern = re.compile(r'[XY][+=](\d+)')
    xa = ya = xb = yb = 0
    for line in read_file(Year.y2024,'day13.txt'):
        if not line:
            continue

        if 'Button A' in line:
            matches= re.findall(pattern,line)
            xa,ya=map(int, matches)
        elif 'Button B' in line:
            matches= re.findall(pattern,line)
            xb,yb=map(int, matches)
        else:
            matches= re.findall(pattern,line)
            x,y=map(int, matches)
            machines.append(((xa,ya),(xb,yb),(x,y)))
    return machines

def count_tokens_for_max_wins(add_on):
    tokens=0
    for machine in get_machines():
        (ax,ay),(bx,by),(px,py)=machine[0],machine[1],machine[2]
        px=px+add_on
        py=py+add_on
        if ax*by-ay*bx==0:
            continue
        an= (px*by-py*bx)/(ax*by-ay*bx)
        bn= (px*ay-py*ax)/(bx*ay-by*ax)
        if (an.is_integer() and bn.is_integer() if add_on !=0
            else an.is_integer() and bn.is_integer() and an<=100 and bn<=100):
            tokens+=(3*an+bn)
    print(int(tokens))

def main():
    count_tokens_for_max_wins(0)
    count_tokens_for_max_wins(10000000000000)

if __name__=='__main__':
    main()

"""
AOC Day 8 : https://adventofcode.com/2024/day/8
"""
from collections import defaultdict
from utilities import read_file,Year

def get_antenas():
    """
    creates dictionary of antena locations
    """
    antenas= defaultdict(list)
    lines= read_file(Year.y2024,'day8.txt')
    rows= len(lines)
    cols= len(lines[0]) if lines else 0
    for row,line in enumerate(lines):
        for col,ant in enumerate(line):
            if ant.isalnum():
                antenas[ant].append((row,col))
    return (rows,cols),antenas

def find_antinodes(loc1,loc2,map_size):
    anti_nodes= set()
    r1,c1= loc1
    r2,c2= loc2
    anr1= r1-(r2-r1)
    anr2= r2+(r2-r1)
    anc1= c1-(c2-c1) if c1<c2 else c1+(c1-c2)
    anc2= c2+(c2-c1) if c1<c2 else c2-(c1-c2)
    if anr1>=0 and anr1<map_size[0] and anc1>=0 and anc1<map_size[1]:
        anti_nodes.add((anr1,anc1))
    if anr2>=0 and anr2<map_size[0] and anc2>=0 and anc2<map_size[1]:
        anti_nodes.add((anr2,anc2))
    return anti_nodes

def find_resonant_antinodes(loc1,loc2,map_size):
    anti_nodes= set([loc1,loc2])
    r1,c1= loc1
    r2,c2= loc2
    while r1>=0 and c1>=0 and c1<map_size[1]:
        anr= r1-(r2-r1)
        anc= c1-(c2-c1) if c1<c2 else c1+(c1-c2)
        if anr>=0 and anc>=0 and anc<map_size[1]:
            anti_nodes.add((anr,anc))
        r2,c2=r1,c1
        r1,c1=anr,anc
    r1,c1= loc1
    r2,c2= loc2
    while r2<map_size[0] and c2>=0 and c2<map_size[1]:
        anr= r2+(r2-r1)
        anc= c2+(c2-c1) if c1<c2 else c2-(c1-c2)
        if anr<map_size[0] and anc>=0 and anc<map_size[1]:
            anti_nodes.add((anr,anc))
        r1,c1=r2,c2
        r2,c2=anr,anc
    return anti_nodes

def solution(is_part2):
    map_size,antenas= get_antenas()
    anti_nodes= set()
    for _,locations in antenas.items():
        for i in range(len(locations)):
                for j in range(i+1,len(locations)):
                    if is_part2:
                        nodes=find_resonant_antinodes(locations[i],locations[j],map_size)
                    else:
                        nodes=find_antinodes(locations[i],locations[j],map_size)
                    anti_nodes.update(nodes)
    print(len(anti_nodes))

def main():
    solution(False)
    solution(True)

if __name__=='__main__':
    main()

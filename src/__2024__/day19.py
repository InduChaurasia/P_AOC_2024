"""AOC day 19 : https://adventofcode.com/2024/day/19"""
from utilities import read_file,Year

def read_input():
    is_pattern = False
    towels,patterns=[],[]
    for line in read_file(Year.y2024,'day19.txt'):
        if not line:
            is_pattern = True
            continue
        if is_pattern:
            patterns.append(line)
        else:
            towels.extend(line.split(','))
    towels=[s.replace(" ", "") for s in towels]
    return towels,patterns
 
def count_possible_patterns(towels,pattern,cached={}):
    if not pattern:
        return 1
    if pattern not in cached:  
        t_count=0
        for towel in towels:
            if pattern.startswith(towel):
                next_pattern=pattern.replace(towel,'',1)
                count=count_possible_patterns(towels,next_pattern)
                t_count+=count
        cached[pattern]=t_count
    return cached[pattern]
    

def possible_pattern(towels,patterns):
    possibilities_count=0
    possible_count=0
    for pattern in patterns:
        count=count_possible_patterns(towels,pattern)
        possibilities_count+=count
        if count>0:
            possible_count+=1
    print(f"Possible patterns count: {possible_count}")
    print(f"Sum of possibilities: {possibilities_count}")

def main():
    towels,patterns=read_input()
    possible_pattern(towels,patterns)

if __name__ == "__main__":
    main()
 

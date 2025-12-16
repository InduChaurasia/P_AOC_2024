'''https://adventofcode.com/2025/day/12'''
import re
from utilities import read_file, Year


def read_input():
    data = []
    for line in read_file(Year.y2025, 'day12.txt'):
        data.append(list(map(int, re.findall(r'\d+', line))))
    return data


'''Solution from https://www.youtube.com/watch?v=kjAAoG8jR5M'''


def part1():
    count = 0
    for r, c, *gifts in read_input():
        n = (r//3)*(c//3)
        if n >= sum(gifts):
            count += 1
    print(count)


def main():
    part1()


if __name__ == '__main__':
    main()

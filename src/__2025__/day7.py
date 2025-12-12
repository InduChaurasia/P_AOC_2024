'''https://adventofcode.com/2025/day/7'''
from utilities import read_file, Year


def read_input():
    data = []
    start = None
    for r, line in enumerate(read_file(Year.y2025, 'day7.txt')):
        if 'S' in line:
            start = (r, line.index('S'))
        data.append(list(line))
    return data, start


def count_splitters(data, start) -> int:
    def is_valid_point(p):
        return 0 <= p[0] < len(data) and 0 <= p[1] < len(data[0])
    split_directions = [(0, -1), (0, 1)]
    stack = [start]
    spliters = set()
    visited = set()
    while stack:
        p = stack.pop()
        if p in visited:
            continue
        visited.add(p)

        p = (p[0] + 1, p[1])
        while is_valid_point(p) and data[p[0]][p[1]] == '.':
            p = (p[0] + 1, p[1])

        if is_valid_point(p) and data[p[0]][p[1]] == '^':
            spliters.add(p)
            for d in split_directions:
                np = (p[0] + d[0], p[1] + d[1])
                if is_valid_point(np):
                    stack.append(np)
    return len(spliters)


def find_possible_paths(data, start):
    def is_valid_point(p):
        return 0 <= p[0] < len(data) and 0 <= p[1] < len(data[0])
    cache = {}

    def paths(p) -> int:
        if not is_valid_point(p):
            return 1
        if p in cache:
            return cache[p]
        c = 0
        if data[p[0]][p[1]] in ('.', 'S'):
            c = paths((p[0]+1, p[1]))
        elif data[p[0]][p[1]] == '^':
            c = paths((p[0]+1, p[1]-1)) + paths((p[0]+1, p[1]+1))
        cache[p] = c
        return c
    return paths(start)


def main():
    data, start = read_input()
    print(count_splitters(data, start))
    print(find_possible_paths(data, start))


if __name__ == '__main__':
    main()

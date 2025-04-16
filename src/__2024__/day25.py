"""AOC day 25: https://adventofcode.com/2024/day/25"""

from utilities import read_file,Year

def read_input():
    locks, keys = [], []
    current, is_lock = [], True

    for line in read_file(Year.y2024, 'day25.txt'):
        if not line:
            if current:
                (locks if is_lock else keys).append(current)
                current = []
            continue
        if not current:
            is_lock = '.' not in line
        current.append(list(line))

    if current:
        (locks if is_lock else keys).append(current)

    return locks, keys

def do_fit(lock,key):
    rows= len(lock)
    cols= len(lock[0])
    for i in range(rows):
        for j in range(cols):
            if lock[i][j] == '#' and key[i][j] == '#':
                return False
    return True

def find_fitting_keys():
    locks,keys=read_input()
    fit=0
    for lock in locks:
        for key in keys:
            if do_fit(lock,key):
                fit+=1
    print(fit)

def main():
    find_fitting_keys()

if __name__ == '__main__':
    main()

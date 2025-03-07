from collections import Counter
from utilities import Year, read_file

def getInput():
    locations1 = []
    locations2= []
    lines  = read_file(Year.y2024, 'day1.txt')
    for line in lines:
        arr = line.split('   ')
        locations1.append(int(arr[0]))
        locations2.append(int(arr[1].rstrip()))

    locations1.sort()
    locations2.sort()
    return locations1, locations2

def solution_part1():
    locations = getInput()
    sum=0
    for i in range(len(locations[0])):
        sum = sum+abs(locations[0][i]-locations[1][i])
    return sum
       
def solution_part2():
    locations = getInput()
    group = Counter(locations[1])
    sum = 0
    for i in locations[0]:
        if i in group:
            sum = sum + group[i]*i
    return sum

def main():
    part1 = solution_part1()
    part2 = solution_part2()
    print('part1: ' ,part1)
    print('part2: ', part2)

if __name__=='__main__':
    main()
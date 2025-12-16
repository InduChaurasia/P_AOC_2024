'''https://adventofcode.com/2025/day/10'''

from utilities import read_file, Year


def read_input():
    data = []

    for line in read_file(Year.y2025, 'day10.txt'):
        arr = line.split(' ')
        pattern = list(arr[0][1:len(arr[0])-1])
        buttons = []
        for s in arr[1:len(arr)-1]:
            s = s[1:len(s)-1]
            buttons.append(list(map(int, s.split(','))))
        joltages = list(map(int, arr[-1][1:len(arr[-1])-1].split(',')))
        data.append((pattern, buttons, joltages))
    return data


def fewest_press_sum_for_light(data):
    sum = 0
    for p, buttons, _ in data:
        cp = ['.']*len(p)
        sum += fewest_press_for_light(p, cp, buttons, 0, 0)
    return sum


def fewest_press_for_light(p, cp, buttons, bi, pressed_buttons):

    if cp == p:
        return pressed_buttons
    if bi >= len(buttons):
        return float('inf')
    # press button at index bi
    np = list(cp)
    for b in buttons[bi]:
        np[b] = '.' if np[b] == '#' else '#'
    n1 = fewest_press_for_light(p, np, buttons, bi+1, pressed_buttons+1)
    # do not press button at index bi
    n2 = fewest_press_for_light(p, cp, buttons, bi+1, pressed_buttons)
    return min(n1, n2)


def main():
    data = read_input()
    print(fewest_press_sum_for_light(data))


if __name__ == '__main__':
    main()

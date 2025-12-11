'''https://adventofcode.com/2025/day/11'''

from utilities import read_file, Year


def get_input():
    device_outputs = {}
    for line in read_file(Year.y2025, 'day11.txt'):
        i = line.index(':')
        device = line[:i]
        outputs = [o for o in line[i+1:].split(' ') if o != '']
        device_outputs[device] = outputs
    return device_outputs


def find_paths(device_outputs, start, end):
    cache = {}

    def recursion(device, path):
        if device == end:
            return 1
        if device not in cache:
            outputs = device_outputs[device] if device in device_outputs else [
            ]
            paths = 0
            for next_device in outputs:
                paths += recursion(next_device, path+[device])
            cache[device] = paths
        return cache[device]
    return recursion(start, [])


def part1(device_outputs):
    return find_paths(device_outputs, 'you', 'out')


def part2(device_outputs):
    c1 = find_paths(device_outputs, 'svr', 'fft')*find_paths(device_outputs,
                                                             'fft', 'dac')*find_paths(device_outputs, 'dac', 'out')
    c2 = find_paths(device_outputs, 'svr', 'dac')*find_paths(device_outputs,
                                                             'dac', 'fft')*find_paths(device_outputs, 'fft', 'out')
    return c1+c2


def main():
    device_outputs = get_input()
    print(part1(device_outputs))
    print(part2(device_outputs))


if __name__ == '__main__':
    main()

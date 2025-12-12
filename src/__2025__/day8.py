'''http://adventofcode.com/2025/day/8'''

from utilities import read_file, Year
import math


def read_points() -> list[list[int]]:
    return [list(map(int, line.split(','))) for line in read_file(Year.y2025, 'day8.txt')]


def find_distances(points):
    l = len(points)
    distances = {}
    for i in range(0, l-1):
        x1, y1, z1 = points[i]
        for j in range(i+1, l):
            x2, y2, z2 = points[j]
            dist = (x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2
            distances[dist] = (i, j)
    return distances


def join_boxes(box1, box2, circuits, box_circuit, circuit_count):
    c1 = box_circuit[box1] if box1 in box_circuit else ''
    c2 = box_circuit[box2] if box2 in box_circuit else ''
    modified_circuit = None
    if c1 and c1 == c2:
        return modified_circuit, circuit_count
    elif not c1 and not c2:
        circuit_name = 'C'+str(circuit_count)
        circuits[circuit_name] = [box1, box2]
        box_circuit[box1] = circuit_name
        box_circuit[box2] = circuit_name
        circuit_count += 1
        modified_circuit = circuit_name
    elif not c1:
        circuits[c2].append(box1)
        box_circuit[box1] = c2
        modified_circuit = c2
    elif not c2:
        circuits[c1].append(box2)
        box_circuit[box2] = c1
        modified_circuit = c1
    else:
        l1, l2 = len(circuits[c1]), len(circuits[c2])
        to_circuit = c1 if l1 > l2 else c2
        from_circuit = c1 if l1 <= l2 else c2
        from_boxes = circuits[from_circuit]
        circuits[to_circuit] = circuits[to_circuit]+from_boxes
        modified_circuit = to_circuit
        del circuits[from_circuit]
        for b in from_boxes:
            box_circuit[b] = to_circuit
    return modified_circuit, circuit_count


def find_circuits_after_n_joins(n, distances):
    circuits = {}
    box_circuit = {}
    circuit_count = 1
    join = 0
    for d in sorted(distances.keys()):
        if join < n:
            join += 1
            box1, box2 = distances[d]
            _, circuit_count = join_boxes(
                box1, box2, circuits, box_circuit, circuit_count)
    circuit_lengths = []
    for c in circuits.values():
        circuit_lengths.append(len(c))
    circuit_lengths.sort()
    last_three = circuit_lengths[len(circuit_lengths)-3:len(circuit_lengths)]
    return math.prod(last_three)


def find_last_two_boxes(points, distances):
    circuits = {}
    box_circuit = {}
    circuit_count = 1
    max_circuit_size = 0
    result = 0
    for d in sorted(distances.keys()):
        box1, box2 = distances[d]
        modified_circuit, circuit_count = join_boxes(
            box1, box2, circuits, box_circuit, circuit_count)
        if modified_circuit:
            max_circuit_size = max(
                max_circuit_size, len(circuits[modified_circuit]))
            if max_circuit_size == len(points):
                print(f'{box1},{box2}')
                result = points[box1][0]*points[box2][0]
                break
    return result


def main() -> None:
    points = read_points()
    distances = find_distances(points)
    print(f'Part 1: {find_circuits_after_n_joins(1000, distances)}')
    print(f'Part 2: {find_last_two_boxes(points, distances)} ')


if __name__ == '__main__':
    main()

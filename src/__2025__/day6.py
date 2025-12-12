'''https://adventofcode.com/2025/day/6'''

from utilities import read_file, Year


def read_input_part1() -> list[list[str]]:
    lines = read_file(Year.y2025, 'day6.txt')
    m = []
    for line in lines:
        row = []
        for x in line.split(' '):
            if not x:
                continue
            row.append(x)
        m.append(row)
    return m


def perform_operation(op: str, val1: int, val2: int) -> int:
    if op == '+':
        return val1 + val2
    elif op == '*':
        return val1 * val2
    else:
        raise ValueError(f"Unknown operation: {op}")


def find_columns(data: list[list[str]]) -> list[tuple[int, int]]:
    r = len(data)
    c = len(data[0])
    columns = []
    start = 0
    for j in range(c):
        is_valid = True
        for i in range(r):
            if data[i][j].isdigit() or data[i][j] in '+*':
                is_valid = False
                break
        if is_valid:
            columns.append((start, j))
            start = j+1
    columns.append((start, c))
    return columns


def problem_result_part1() -> int:
    data = read_input_part1()
    result = 0
    r = len(data)
    c = len(data[0])

    for j in range(c):
        operation = data[r-1][j]
        problem_j_result = 0 if operation == '+' else 1
        for i in range(r-1):
            problem_j_result = perform_operation(
                operation, problem_j_result, int(data[i][j]))
        result += problem_j_result
    return result


def problem_result_part2() -> int:
    lines = read_file(Year.y2025, 'day6.txt', False)
    data = [list(line.replace("\n", "")) for line in lines]

    last_line = lines[-1].replace(' ', '')

    column_ranges = find_columns(data)
    operations = list(last_line)

    result = 0
    for index, (start, end) in enumerate(column_ranges):
        operation = operations[index]
        result_for_col = 0 if operation == '+' else 1
        for k in range(end-1, start-1, -1):
            current_digit = ''
            for i in range(len(data)-1):
                if data[i][k].isdigit():
                    current_digit += data[i][k]
            if current_digit:
                result_for_col = perform_operation(
                    operation, result_for_col, int(current_digit))
        result += result_for_col
    return result


def main():
    print(problem_result_part1())
    print(problem_result_part2())


if __name__ == '__main__':
    main()

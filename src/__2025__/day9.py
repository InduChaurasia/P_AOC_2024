'''https://adventofcode.com/2025/day/9'''

from utilities import read_file, Year


def read_coordinates():
    tiles = []
    rm, cm = float('inf'), float('inf')
    for line in read_file(Year.y2025, 'day9.txt'):
        c, r = line.split(',')
        rm, cm = min(int(r), rm), min(int(c), cm)
        tiles.append((int(r), int(c)))

    return list((r-rm, c-cm) for (r, c) in tiles)


def max_area_rectangle(red_tiles: list[tuple[int, int]]) -> int:
    l = len(red_tiles)
    max_area = 0
    for i in range(l):
        x1, y1 = red_tiles[i]
        for j in range(i+1, l):
            x2, y2 = red_tiles[j]
            area = (abs(x2-x1)+1)*(abs(y2-y1)+1)
            max_area = max(area, max_area)
    return max_area


def max_area_rectangle_only_tiles(red_tiles: list[tuple[int, int]]) -> int:
    # original to compact row
    r_to_R = {0: 0}
    # compact to original row
    R_to_r = {0: 0}
    # original to compact column
    c_to_C = {0: 0}
    # compact to original column
    C_to_c = {0: 0}

    def compact_points(red_tiles):
        clone = list(red_tiles)
        clone.sort()
        rma = 0
        for r, c in clone:
            nr = lr+2 if r not in r_to_R else r_to_R[r]
            r_to_R[r] = nr
            R_to_r[nr] = r
            rma = max(rma, nr)
            lr = nr

        clone.sort(key=lambda p: p[1])
        cma = 0
        for r, c in clone:
            nc = lc+2 if c not in c_to_C else c_to_C[c]
            c_to_C[c] = nc
            C_to_c[nc] = c
            cma = max(cma, nc)
            lc = nc

        for i, (r, c) in enumerate(red_tiles):
            red_tiles[i] = (r_to_R[r], c_to_C[c])
        return rma, cma

    r, c = compact_points(red_tiles)
    matrix = create_tile_matrix(red_tiles, r, c)
    l = len(red_tiles)
    max_area = 0
    for i in range(l-1):
        x1, y1 = red_tiles[i]
        # find the original points
        x1, y1 = R_to_r[x1], C_to_c[y1]
        for j in range(i+1, l):
            x2, y2 = red_tiles[j]
            # find the original points
            x2, y2 = R_to_r[x2], C_to_c[y2]
            area = (abs(x2-x1)+1)*(abs(y2-y1)+1)
            if area > max_area and is_tile_rectangle(red_tiles[i], red_tiles[j], matrix, red_tiles):
                max_area = area
    return max_area


def create_tile_matrix(red_tiles: list[tuple[int, int]], r: int, c: int) -> list[list[int]]:
    matrix = []
    for i in range(r+1):
        row = []
        for j in range(c+1):
            row.append('#' if (i, j) in red_tiles else '.')
        matrix.append(row)

    red_tiles.append(red_tiles[0])
    p1 = red_tiles[0]
    for k in range(1, len(red_tiles)):
        p2 = red_tiles[k]
        if p1[0] == p2[0]:
            r = p1[0]
            r1 = p1[1] if p1[1] < p2[1] else p2[1]
            r2 = p1[1] if p1[1] > p2[1] else p2[1]
            for j in range(r1, r2+1):
                if matrix[r][j] == '#':
                    continue
                matrix[r][j] = 'X'
        else:
            c = p1[1]
            r1 = p1[0] if p1[0] < p2[0] else p2[0]
            r2 = p1[0] if p1[0] > p2[0] else p2[0]
            for i in range(r1, r2+1):
                if matrix[i][c] == '#':
                    continue
                matrix[i][c] = 'X'
        p1 = p2
    return matrix


def is_tile_rectangle(p1, p2, matrix, red_tiles) -> bool:
    r1 = p1[0] if p1[0] < p2[0] else p2[0]
    r2 = p1[0] if p1[0] > p2[0] else p2[0]
    c1 = p1[1] if p1[1] < p2[1] else p2[1]
    c2 = p1[1] if p1[1] > p2[1] else p2[1]
    for r in range(r1, r2+1):
        for c in range(c1, c2+1):
            if matrix[r][c] in ['X', '#']:
                continue
            if not is_point_inside_polygon((r, c), red_tiles):
                return False
            matrix[r][c] = 'X'
    return True


def is_point_inside_polygon(p, red_tiles) -> bool:
    e1 = red_tiles[0]
    count = 0
    for e2 in red_tiles:
        if e1 == e2:
            continue
        if is_point_crossing_edge(e1, e2, p):
            count += 1
        e1 = e2
    return count % 2 != 0


def is_point_crossing_edge(e1, e2, point) -> bool:
    y1, x1 = e1 if e1[0] < e2[0] else e2
    y2, x2 = e2 if e1[0] < e2[0] else e1
    yp, xp = point
    return (yp < y1) != (yp < y2) and xp < x1+((yp-y1)/(y2-y1))*(x2-x1)


def main():
    red_tiles = read_coordinates()
    print(max_area_rectangle(red_tiles))
    print(max_area_rectangle_only_tiles(red_tiles))


if __name__ == '__main__':
    main()

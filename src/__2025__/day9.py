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
    r_to_cr = {0: 0}
    # compact to original row
    cr_to_r = {0: 0}
    # original to compact column
    c_to_cc = {0: 0}
    # compact to original column
    cc_to_c = {0: 0}

    def compact_points(red_tiles):
        rs = sorted({r for r, _ in red_tiles})
        cs = sorted({c for _, c in red_tiles})
        for r in rs:
            nr = lr+1 if r not in r_to_cr else r_to_cr[r]
            r_to_cr[r] = nr
            cr_to_r[nr] = r
            lr = nr
        for c in cs:
            nc = lc+1 if c not in c_to_cc else c_to_cc[c]
            c_to_cc[c] = nc
            cc_to_c[nc] = c
            lc = nc

        compact_tiles = [(r_to_cr[r], c_to_cc[c]) for r, c in red_tiles]
        return compact_tiles

    red_tiles = compact_points(red_tiles)
    matrix = create_matrix_with_red_tiles(red_tiles)
    matrix = fill_green_tile_edge(matrix, red_tiles)
    l = len(red_tiles)
    max_area = 0
    for i in range(l-1):
        x1, y1 = red_tiles[i]
        # find the original points
        x1, y1 = cr_to_r[x1], cc_to_c[y1]
        for j in range(i+1, l):
            x2, y2 = red_tiles[j]
            # find the original points
            x2, y2 = cr_to_r[x2], cc_to_c[y2]
            area = (abs(x2-x1)+1)*(abs(y2-y1)+1)
            if area > max_area and is_rectangle_of_tiles(red_tiles[i], red_tiles[j], matrix, red_tiles):
                max_area = area
    return max_area


def create_matrix_with_red_tiles(red_tiles: list[tuple[int, int]]) -> list[list[int]]:
    r = sorted({r for r, _ in red_tiles})[-1]+1
    c = sorted({c for _, c in red_tiles})[-1]+1
    matrix = [['#' if (i, j) in red_tiles else '.' for j in range(c)]
              for i in range(r)]
    return matrix


def fill_green_tile_edge(matrix, red_tiles):
    red_tiles.append(red_tiles[0])
    p1 = red_tiles[0]
    for p2 in red_tiles:
        if p1 == p2:
            continue
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


def is_rectangle_of_tiles(p1, p2, matrix, red_tiles) -> bool:
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

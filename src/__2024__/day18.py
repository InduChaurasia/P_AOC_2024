"""AOC day18: https://adventofcode.com/2024/day/18"""
import heapq
from utilities import read_file,Year

def get_input():
    return [tuple(map(int,line.split(','))) for line in read_file(Year.y2024, 'day18.txt')]

def fill_bytes(m_bytes,size,byte_count):
    maze = [['.' for _ in range(size+1)] for _ in range(size+1)]
    for i in range(byte_count):
        y,x = m_bytes[i]
        maze[x][y] = '#'
    return maze

def shortest_exit_path(maze):
    r,c=len(maze),len(maze[0])
    directions = [(0,1),(1,0),(0,-1),(-1,0)]
    q=[]
    heapq.heappush(q,(0,(0,0)))
    visited=set()
    while q:
        path_len,(cr,cc)=heapq.heappop(q)
        if (cr,cc) in visited:
            continue
        visited.add((cr,cc))
        if cr==r-1 and cc==c-1:
            return path_len
        for dr,dc in directions:
            nr,nc=cr+dr,cc+dc
            if 0<=nr<r and 0<=nc<c and maze[nr][nc]!='#' and (nr,nc) not in visited:
                heapq.heappush(q,(path_len+1,(nr,nc)))
    return -1
def shortest_path_after_bytes(maze_size,byte_count):
    maze = fill_bytes(get_input(),maze_size,byte_count)
    path=shortest_exit_path(maze)
    print(f'shortest exit path length: {path}')

def first_byte_for_no_exit(maze_size):
    byte_count=1025
    m_bytes=get_input()
    maze = fill_bytes(m_bytes,maze_size,byte_count)
    path=shortest_exit_path(maze)
    while path!=-1 and byte_count<len(m_bytes):
        (y,x)=m_bytes[byte_count]
        byte_count+=1
        maze[x][y]='#'
        path=shortest_exit_path(maze)
    print(f'first byte for no exit: {m_bytes[byte_count-1]}')

def main():
    shortest_path_after_bytes(70,1024)
    first_byte_for_no_exit(70)

if __name__=='__main__':
    main()

"""AOC day20: https://adventofcode.com/2024/day/20"""
from collections import deque
from utilities import read_file,Year

def get_maze():
    maze=[]
    for line in read_file(Year.y2024, "day20.txt"):
        maze.append(list(line))
    start=next((i,j) for i,row in enumerate(maze) for j,val in enumerate(row) if val=='S')
    return maze,start

def find_best_path(maze,start):
    r,c=len(maze),len(maze[0])
    directions=[(-1,0),(1,0),(0,-1),(0,1)]
    queue= deque([(start[0], start[1], [])])
    visited=set([start])
    while queue:
        (cr,cc,path)=queue.popleft()
        if maze[cr][cc]=='E':
            path.append((cr,cc))
            return [(x, y, i) for i, (x, y) in enumerate(path)]
        for dr,dc in directions:
            nr,nc=cr+dr,cc+dc
            if 0<=nr<r and 0<=nc<c and maze[nr][nc]!='#' and (nr,nc) not in visited:
                queue.append((nr,nc,path+[(cr,cc)]))
                visited.add((nr,nc))
    return []

def cheat_path_count(max_cheat_time):
    min_save_time=100
    maze,start=get_maze()
    best_path=find_best_path(maze,start)
    path_len = len(best_path)
    count=0
    for i in range(0,path_len-1):
        p1=best_path[i]
        for j in range(i+1,path_len):
            p2=best_path[j]
            cheat_time=abs(p1[0]-p2[0])+abs(p1[1]-p2[1])
            saved_distance=abs(p2[2]-p1[2])
            saved_time=saved_distance-cheat_time
            if 2<=cheat_time<=max_cheat_time and saved_time>=min_save_time:
                count+=1
    print(f'cheat time {max_cheat_time}, no of ways to cheat: {count}')

def main():
    cheat_path_count(2)
    cheat_path_count(20)

if __name__=='__main__':
    main()

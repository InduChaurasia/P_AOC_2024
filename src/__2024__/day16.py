"""AOC day16:https://adventofcode.com/2024/day/16"""
import heapq
from collections import defaultdict
from utilities import read_file,Year

def best_path_score_and_tiles():
    maze=[list(line) for line in read_file(Year.y2024,'day16.txt')]
    start=next((i,j) for i,row in enumerate(maze) for j,val in enumerate(row) if val=='S')
    direction={
        (-1,0):'up',
        (1,0):'down',
        (0,-1):'left',
        (0,1):'right'
        }
    possible_moves={
        'up':((-1,0),(0,-1),(0,1)),
        'down':((1,0),(0,-1),(0,1)),
        'left':((0,-1),(-1,0),(1,0)),
        'right':((0,1),(-1,0),(1,0))
        }
    visited=set()
    paths=defaultdict(set)
    min_score=None

    q=[]
    heapq.heappush(q,(0,(start[0],start[1],'right',[])))
    while q:
        score,(cr,cc,d,pp)=heapq.heappop(q)
        visited.add((cr,cc,d))
        if maze[cr][cc]=='E':
            paths[score].update(pp)
            paths[score].add((cr,cc))
            min_score = min(score, min_score) if min_score is not None else score
            continue
        for (dr,dc) in possible_moves.get(d):
            nr,nc=cr+dr,cc+dc
            nd= direction.get((dr,dc))
            next_score=score+1 if nd==d else score+1001
            if ((nr,nc,nd) not in visited
                and (min_score is None or next_score<=min_score)
                and maze[nr][nc]!='#'):
                pp1=list(pp)
                pp1.append((cr,cc))
                heapq.heappush(q,(next_score,(nr,nc,nd,pp1)))
    best_path_tiles=paths[min_score]
    print(f'min score: {min_score},paths:{len(best_path_tiles)}')

def main():
    best_path_score_and_tiles()

if __name__=='__main__':
    main()

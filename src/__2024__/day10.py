from utilities import read_file,Year

def get_trail_map()->tuple[list[tuple[int,int]],list[tuple[int,int]]]:
    trail:list[tuple[int,int]]=[]
    heads:list[tuple[int,int]]=[]
    for i,line in enumerate(read_file(Year.y2024,'day10.txt')):
        trail.append([])
        for j,c in enumerate(line):
            trail[i].append(c)
            if c=='0':
                heads.append((i,j))
    return trail,heads

def tail_head_score_sum():
    directions= [(-1,0),(1,0),(0,-1),(0,1)]
    trail,heads=get_trail_map()
    score=0
    for head in heads:
        tails=set()
        path=[head]
        visited=set([head])
        while path:
            i,j=path.pop()
            if trail[i][j]=='9':
                tails.add((i,j))
            for dr,dc in directions:
                m,n=i+dr,j+dc
                if m>=0 and m<len(trail) and n>=0 and n<len(trail[0]):
                    if (m,n) not in visited and trail[m][n]!='.' and int(trail[m][n])-int(trail[i][j])==1:
                        path.append((m,n))
                        visited.add((i,j))
        score+=len(tails)
    print(f'distict tail heads: {score}')

def distict_paths():
    directions= [(-1,0),(1,0),(0,-1),(0,1)]
    trail_map,heads=get_trail_map()
    path_count=0
    for head in heads:
        stack=[(head,frozenset([head]))]
        trails=set()
        while stack:
            (i,j),path=stack.pop()
            if trail_map[i][j]=='9':
                trails.add(path)
                continue
            for dr,dc in directions:
                m,n=i+dr,j+dc
                if m>=0 and m<len(trail_map) and n>=0 and n<len(trail_map[0]):
                    if (m,n) not in path and trail_map[m][n]!='.' and int(trail_map[m][n])-int(trail_map[i][j])==1:
                        stack.append(((m,n),path|{(m,n)}))
        path_count+=len(trails)
    print(f'distinct trail paths: {path_count}')

def main():
    tail_head_score_sum()
    distict_paths()

if __name__=='__main__':
    main()

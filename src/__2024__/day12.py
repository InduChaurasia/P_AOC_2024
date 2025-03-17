"""AOC day 12: https://adventofcode.com/2024/day/12"""
from collections import deque
from utilities import read_file,Year

def garden_map():
    return [list(line) for line in read_file(Year.y2024,'day12.txt')]

def fence_directions(i, j, gm):
    directions = []
    r, c = len(gm), len(gm[0])
    if i <= 0 or gm[i][j] != gm[i-1][j]:
        directions.append('up')
    if i >= r-1 or gm[i][j] != gm[i+1][j]:
        directions.append('down')
    if j <= 0 or gm[i][j] != gm[i][j-1]:
        directions.append('left')
    if j >= c-1 or gm[i][j] != gm[i][j+1]:
        directions.append('right')
    return directions

def region_boundries(region,gm):
    r,c=len(gm),len(gm[0])
    plot_fences:dict[tuple[int, int], list[str]] = {}
    boundries=0
    for i in range(r):
        for j in range(c):
            if (i,j) not in region:
                continue
            plot_fences[(i,j)]=fence_directions(i,j,gm)
            for d in plot_fences[(i,j)]:
                if ((d in ('up','down') and d not in plot_fences.get((i,j-1),[]))
                    or (d in ('left','right') and d not in plot_fences.get((i-1,j),[]))):
                    boundries+=1
    return boundries

def find_regions(gm):
    r,c=len(gm),len(gm[0])
    directions = [(1,0),(-1,0),(0,1),(0,-1)]
    regions=[]
    visited_regions=set()
    for i in range(r):
        for j in range(c):
            if (i,j) in visited_regions:
                continue
            plant_type= gm[i][j]
            region_plants=set()
            region_q=deque([(i,j)])

            while region_q:
                m,n=region_q.pop()
                region_plants.add((m,n))
                visited_regions.add((m,n))
                for dr,dc in directions:
                    ci,cj=m+dr,n+dc
                    if ci>=0 and ci<r and cj>=0 and cj<c and gm[ci][cj]==plant_type and (ci,cj) not in region_plants:
                        region_q.append((ci,cj))
            regions.append((plant_type,region_plants))
    return regions

def fence_price():
    gm=garden_map()
    fence_cost=0
    for _,plants in find_regions(gm):
        fence=sum(len(fence_directions(i,j,gm)) for i,j in plants)
        fence_cost+=fence*len(plants)
    print(f'fence cost: {fence_cost}')

def discounted_fence_price():
    gm=garden_map()
    fence_cost=0
    for _,plants in find_regions(gm):
        b=region_boundries(plants,gm)
        fence_cost+=b*len(plants)
    print(f'discounted fence cost: {fence_cost}')

def main():
    fence_price()
    discounted_fence_price()

if __name__=='__main__':
    main()

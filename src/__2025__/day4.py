'''https://adventofcode.com/2025/day/4 '''
from utilities import read_file,Year

def readinput()-> list[list[str]]:
    return [ list(x) for x in read_file(Year.y2025, "day4.txt")]

def accessible_roll(grid:list[list[str]]) -> list[int]:
    
    r,c=len(grid),len(grid[0])
    directions=[(0,1),(1,0),(-1,0),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)]
    def is_valid_index(x:int,y:int)->bool:
            return 0<=x<r and 0<=y<c
    accessible=[]
    for i in range(r):
        for j in range(c):
            if grid[i][j]=='.':
                 continue
            neighbours=0
            for dx,dy in directions:
                x,y=i+dx,j+dy
                if is_valid_index(x,y) and grid[x][y]=='@':
                    neighbours+=1
            if neighbours<4:
                accessible.append((i,j))
    return accessible

def accessible_role_with_cleanup(grid:list[list[str]]) -> int:
    accessible=accessible_roll(grid)
    count=len(accessible)
    total_count=count
    while count>0:
        for i,j in accessible:
            grid[i][j]='.'
        accessible=accessible_roll(grid)
        count=len(accessible)
        total_count+=count
    return total_count

def main():
    grid=readinput()
    print(len(accessible_roll(grid)))
    print(accessible_role_with_cleanup(grid))

if __name__ == "__main__":
    main()
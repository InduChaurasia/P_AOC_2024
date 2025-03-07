from utilities import read_file,Year
import re

def is_safe(levels):
    bad_index = -1
    for i in range (1,len(levels)):
        if abs(levels[i-1]-levels[i])<1 or abs(levels[i-1]-levels[i])>3:
            bad_index = i
            break
        elif i>=2 and ((levels[i-2]-levels[i-1]>=0 and levels[i-1]-levels[i]<0) or (levels[i-2]-levels[i-1] <0 and levels[i-1]-levels[i]>=0)):
            bad_index = i
            break
    return bad_index==-1, bad_index

def safe_levels():
    input = read_file(Year.y2024,'day2.txt' )
    
    safe = 0
    for s in input:
        levels = [int(num) for num in re.findall(r'\d+', s)]
        result = is_safe(levels)
        if(result[0]):
            safe+=1 
    print('part1 safe levels: %d'%safe)

def tolerate_safe_levels():
    input = read_file(Year.y2024,'day2.txt' )
    
    safe = 0
    for s in input:
        levels = [int(num) for num in re.findall(r'\d+', s)]
        result = is_safe(levels)
        if(result[0]):
            safe+=1 
        else:
            bad_index = result[1]
            levels_copy = levels[:]
            del(levels_copy[bad_index])
            result1 = is_safe(levels_copy)
            result2 = [False,0]
            result3 = [False,0]
            if not result1[0]:
                levels_copy = levels[:]
                del(levels_copy[bad_index-1])
                result2 = is_safe(levels_copy)
            if bad_index>=2 and not result2[0]:
                levels_copy = levels[:]
                del(levels_copy[bad_index-2])
                result3 = is_safe(levels_copy)

            if result1[0] or result2[0] or result3[0]:  
                safe+=1
    print('part2 safe levels: %d'%safe)

def main():
    safe_levels()
    tolerate_safe_levels()

if __name__=='__main__':
     main()

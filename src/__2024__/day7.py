"""
AOC day7 https://adventofcode.com/2024/day/7
"""
from utilities import read_file,Year

def get_equations():
    equations= []
    for line in read_file(Year.y2024,'day7.txt'):
        arr= line.split(":")
        r= int(arr[0].rstrip())
        vals= [int(x) for x in arr[1].lstrip().split(' ')]
        equations.append((r,vals))
    return equations

def find_true_equations(part2):
    sum=0
    for eq in get_equations():
        if calculate(eq,0,0,part2):
            sum+=eq[0]
    print(f'sum of true equations results {sum}')

def calculate(eq,result,index,is_part2):
    expected_result,vals= eq
    if index< len(vals):
        r1= result+vals[index]
        b1= calculate(eq,r1,index+1,is_part2)
        r2= vals[index] if index==0 else result*vals[index]
        b2= calculate(eq,r2,index+1,is_part2)
        if is_part2:
            r3= vals[index] if index==0 else int(str(result)+str(vals[index]))
            b3 = calculate(eq,r3,index+1,is_part2)
            return b1 or b2 or b3
        return b1 or b2
    return result==expected_result

def main():
    find_true_equations(False)
    find_true_equations(True)

if __name__=='__main__':
    main()

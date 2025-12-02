'''https://adventofcode.com/2025/day/2'''
from utilities import read_file,Year

def getInputData():
    line=read_file(Year.y2025,'day2.txt')[0]
    return [r.split('-') for r in line.split(',')]

def invalid_product_ids1(data):
    invalid_ids=[]
    for r in data:
        start=int(r[0])
        end=int(r[1])
        for pid in range(start,end+1):
            pid_str=str(pid)
            l=len(pid_str)
            if l%2==0 and pid_str[:l//2]==pid_str[l//2:]:
                invalid_ids.append(pid)      
    return invalid_ids

def invalid_product_ids2(data):
    invalid_ids=[]
    for r in data:
        start=int(r[0])
        end=int(r[1])
        for pid in range(start,end+1):
            pid_str=str(pid)
            l=len(pid_str)
            for i in range(1,l//2+1):
                r=pid_str.replace(pid_str[:i],'')
                if not r:
                    invalid_ids.append(pid)
                    break           
    return invalid_ids

def sum_invalid_product_ids(is_part_one=True):
    data=getInputData()
    invalid_ids=invalid_product_ids1(data) if is_part_one else invalid_product_ids2(data)
    return sum(invalid_ids)

def main():
    print(sum_invalid_product_ids())
    print(sum_invalid_product_ids(False))

if __name__ == "__main__":
    main()
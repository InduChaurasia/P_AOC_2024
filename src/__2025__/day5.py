'''https://adventofcode.com/2025/day/5'''
from utilities import read_file,Year

def read_input():
    ranges = []
    product_ids=[]

    for line in  read_file(Year.y2025, 'day5.txt'):
        if not line:
            continue
        if '-' in line:
            start,end = line.split('-')
            ranges.append( (int(start), int(end)) )
        else:
            product_ids.append(int(line))
        ranges.sort()
    return ranges, product_ids

def find_product_id(ranges,product_id,s,e)->str:
    if e in (s,s+1):
        return  ranges[s][0]<=product_id<=ranges[s][1] or ranges[e][0]<=product_id<=ranges[e][1]
    mid = (s+e)//2
    return find_product_id(ranges,product_id,s,mid) or find_product_id(ranges,product_id,mid+1,e)

def fresh_inventrory(ranges,product_ids)->int:
    fresh= 0
    for product_id in product_ids:
        if find_product_id(ranges,product_id,0,len(ranges)-1):
            fresh+=1
    return fresh

def fresh_product_ids(ranges)->int:
    merged_ranges=[ranges[0]]
    for i in range(1,len(ranges)):
        s,e = ranges[i]
        last_s,last_e = merged_ranges[-1]
        if s<=last_e:
            merged_ranges[-1]=(last_s,max(e,last_e))
        else:
            merged_ranges.append( (s,e) )
    product_id_count=0
    for s,e in merged_ranges:
        product_id_count+=e - s + 1
    return product_id_count

def main():
    ranges,product_ids = read_input()
    print(f'fresh inventry: {fresh_inventrory(ranges,product_ids)}')
    print(f'fresh product ids: {fresh_product_ids(ranges)}')

if __name__ == '__main__':
    main()
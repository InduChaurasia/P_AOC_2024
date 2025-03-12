from utilities import read_file,Year
from typing import List,Tuple

def read_disk_map():
    lines= read_file(Year.y2024,'day9.txt')
    s= "\n".join(line.strip() for line in lines)
    return s

def expand_disk_map()->Tuple[List[int],List[int]]:
    expanded_map=[]
    block_len=[]
    s=read_disk_map()
    for index,c in enumerate(s):
        n = int(c)
        block_len.append(n)
        while n>0:
            map_index= index//2 if index%2==0 else -(index//2 +1)
            expanded_map.append(map_index)
            n= n-1
    return expanded_map,block_len

def checksum(disk_map:List[int]):
    s=0
    for i,c in enumerate(disk_map):
        if c>=0:
            s+= i*c
    return s

def compact_bit():
    disk_map,_= expand_disk_map()
    i,j=0,len(disk_map)-1
    while i<j:
        while disk_map[i]>=0:
            i=i+1
        while disk_map[j]<0:
            j=j-1

        if i<j:
            t = disk_map[i]
            disk_map[i]= disk_map[j]
            disk_map[j]= t
            i= i+1
            j= j-1
    print(checksum(disk_map))

def compact_block():
    expanded_map,block_len= expand_disk_map()
    for i in range(len(expanded_map)-1,0,-1):
        f= expanded_map[i]
        fli=f*2
        if f<0 or block_len[fli]<=0:
            continue
        fl=block_len[fli]
        for j in range(0,i-fl+1):
            s= expanded_map[j]
            sli=abs(expanded_map[j])*2-1
            if s>=0 or block_len[sli]<=0:
                continue
            sl=block_len[sli]
            if fl<=sl:
                m,n,o=i,j,fl
                while o>0:
                    temp = expanded_map[m]
                    expanded_map[m]=expanded_map[n]
                    expanded_map[n]=temp
                    o,m,n=o-1,m-1,n+1
                block_len[sli]= block_len[sli]-fl
                block_len[fli]= 0
                break
    print(checksum(expanded_map))
    
def main():
    compact_bit()
    compact_block()

if __name__=='__main__':
    main()

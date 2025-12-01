from utilities import Year, read_file
from node import Node


def getInput():
    lines  = read_file(Year.y2025, 'day1.txt')
    rotations= [(line[0:1],line[1:]) for line in lines]
    return rotations

def circular_double_linked_list(size:int,mid:int)->Node:
    head=Node(0)
    current=head
    start=head
    for i in range(1,size):
        new_node=Node(i)
        if i == mid:
            start=new_node
        current.next=new_node
        new_node.prev=current
        current=new_node
        
    current.next=head
    head.prev=current
    return start

def solution(is_part_1:bool)->int:
    node = circular_double_linked_list(100,50)
    rotations = getInput()
    count=0
    for direction,steps in rotations:
        steps=int(steps)
        for _ in range(steps):
            if direction=='R':
                node=node.next
            else:
                node=node.prev
            if node.data==0 and not is_part_1:
                count+=1
        if is_part_1 and node.data==0:
            count+=1
    print(f"Number of times at position 0: {count}")
    return count
   

def main():
    solution(is_part_1=True)
    solution(is_part_1=False)
    
if __name__=='__main__':
    main()
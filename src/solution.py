from typing import List, Optional
from collections import Counter,defaultdict
import math
from utilities import Year, read_file

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def minDistance(self, word1: str, word2: str) -> int: 
        if not word1 and not word2:
            return 0
        if word1==word2:
            return 0
        
        r,c= len(word2)+1, len(word1)+1
        m = [[0 for _ in range(c)] for _ in range(r) ]
        for i in range(r):
            m[i][0]=i
        for j in range(c):
            m[0][j]=j
        for i in range(1,r):
            for j in range(1,c):
                print(f'{i},{j}')
                operations = min (m[i-1][j],m[i-1][j-1],m[i][j-1])
                if word1[j-1]!=word2[i-1]:
                    operations+=1
                m[i][j]=operations
               
        for i in range(r):
            print(m[i])
        return m[r-1][c-1]
        

        
   

def main():
    s=Solution()
    word1 = "aa"
    word2 = "a"
    s.minDistance(word1,word2)
   
    

if __name__ == "__main__":
        main()

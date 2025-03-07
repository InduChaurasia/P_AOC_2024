from utilities import read_file,Year

def format_input():
    matrix = []
    for line in read_file(Year.y2024,'day4.txt'):
        arr = list(line)
        matrix.append(arr)
    return matrix

def count_xmas():
    matrix = format_input()
    count = 0
    r = len(matrix)
    c = len(matrix[0])
    for i in range(r):
        for j in range(c):
            if(matrix[i][j] == 'X'):
                if(i-3>=0 and matrix[i-1][j] == 'M' and matrix[i-2][j] == 'A' and matrix[i-3][j] == 'S'):
                   count += 1
                if(i+3<r and matrix[i+1][j] == 'M' and matrix[i+2][j] == 'A' and matrix[i+3][j] == 'S'):
                   count += 1
                if(j-3>=0 and matrix[i][j-1] == 'M' and matrix[i][j-2] == 'A' and matrix[i][j-3] == 'S'):
                   count += 1
                if(j+3<c and matrix[i][j+1] == 'M' and matrix[i][j+2] == 'A' and matrix[i][j+3] == 'S'):
                    count += 1
                if(i+3<r and j+3<c and matrix[i+1][j+1] == 'M' and matrix[i+2][j+2] == 'A' and matrix[i+3][j+3] == 'S'):
                    count += 1
                if(i-3>=0 and j-3>=0 and matrix[i-1][j-1] == 'M' and matrix[i-2][j-2] == 'A' and matrix[i-3][j-3] == 'S'):
                    count += 1
                if(i+3<r and j-3>=0 and matrix[i+1][j-1] == 'M' and matrix[i+2][j-2] == 'A' and matrix[i+3][j-3] == 'S'):
                    count += 1
                if(i-3>=0 and j+3<c and matrix[i-1][j+1] == 'M' and matrix[i-2][j+2] == 'A' and matrix[i-3][j+3] == 'S'):
                    count += 1  
    print(f'XMAS appears {count} times')

def valid_x_mas_index(i,j,r,c):
    return i-1>=0 and i+1<r and j-1>=0 and j+1<c

def count_x_mas():
    matrix = format_input()
    count = 0
    r = len(matrix)
    c = len(matrix[0])
    for i in range(r):
        for j in range(c):
            if(matrix[i][j]=='A'):
                if(valid_x_mas_index(i,j,r,c)):
                    if(matrix[i-1][j-1]=='M' and matrix[i-1][j+1]=='S' and matrix[i+1][j-1]=='M' and matrix[i+1][j+1]=='S'):
                        count += 1
                    if(matrix[i-1][j-1]=='M' and matrix[i-1][j+1]=='M' and matrix[i+1][j-1]=='S' and matrix[i+1][j+1]=='S'):
                        count += 1  
                    if(matrix[i-1][j-1]=='S' and matrix[i-1][j+1]=='M' and matrix[i+1][j-1]=='S' and matrix[i+1][j+1]=='M'):
                        count += 1
                    if(matrix[i-1][j-1]=='S' and matrix[i-1][j+1]=='S' and matrix[i+1][j-1]=='M' and matrix[i+1][j+1]=='M'):
                        count += 1
    print(f'X-MAS appears {count} times')

                
def main():
    count_xmas()
    count_x_mas()
    
if __name__ == '__main__':
    main()
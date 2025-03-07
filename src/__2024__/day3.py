import re
from utilities import Year,read_file

def mul_sum():
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    input =''.join(read_file(Year.y2024, "day3.txt"))
    sum=0
    for num1,num2 in re.findall(pattern,input):
        sum = sum + int(num1)*int(num2)
    print(f'part1 sum: {sum}')

def enabled_mul_sum():
    pattern = r"(do\(\))|(don't\(\))|mul\((\d{1,3}),(\d{1,3})\)"
    input =''.join(read_file(Year.y2024, "day3.txt"))
    sum=0
    enabled = True
    for match in re.finditer(pattern,input):
        if match.group(1):
            enabled = True
        elif match.group(2):
            enabled = False
        elif match.group(3) and enabled:
            sum = sum + int(match.group(3))*int(match.group(4))
    print(f'part2 sum: {sum}')

def main():
    mul_sum()
    enabled_mul_sum()   

if __name__ == "__main__":
    main()
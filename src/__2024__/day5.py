from utilities import read_file,Year
from collections import defaultdict

def read_inputs():
    rules = defaultdict(list)
    prints = []
    for line in read_file(Year.y2024,'day5.txt'):
        if(line == ''):
            continue
        if('|' in line):
            key,val = line.split('|')
            rules[key].append(val)
        else:
            prints.append(line.split(','))
    return rules,prints

def valid_prints_sum():
    rules,prints = read_inputs()
    sum = 0
    for print_ in prints:
        is_valid = True
        for i in range(len(print_)-1):
            for j in range(i+1, len(print_)):
                if (print_[i] in rules and print_[j] not in rules[print_[i]]) or (print_[j] in rules and print_[i] in rules[print_[j]]):
                    is_valid = False
                    break
            if not is_valid:
                break
        if is_valid:
           mid = print_[len(print_)//2]
           sum += int(mid)   
    print(f'valid prints mid values sum : {sum}') 

def fix_invalid_prints_sum(): 
    rules,prints = read_inputs()
    sum = 0
    for print_ in prints:
        was_invalid = False
        for i in range(len(print_)-1):
            j = i+1
            while j<len(print_):
                if (print_[i] in rules and print_[j] not in rules[print_[i]]) or (print_[j] in rules and print_[i] in rules[print_[j]]):
                    was_invalid = True
                    temp = print_[i]
                    print_[i] = print_[j]
                    print_[j] = temp
                    j=i+1
                else:
                    j+=1
                    
        if was_invalid:
           mid = print_[len(print_)//2]
           sum += int(mid)   
    print(f'fixed invalid prints mid values sum : {sum}')     

def main():
    valid_prints_sum()
    fix_invalid_prints_sum()

if __name__=='__main__':
    main()  

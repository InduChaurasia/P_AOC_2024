'''https://adventofcode.com/2025/day/3'''
from utilities import read_file,Year

def read_input()-> list[str]:
    return read_file(Year.y2025, "day3.txt")

def max_joltage_for_bank(no_of_batteries:int,joltage_bank:str)-> int:
    max_joltage=int(joltage_bank[:no_of_batteries])
    for i in range(no_of_batteries,len(joltage_bank)):
        next_joltage=str(max_joltage)+joltage_bank[i] # no_of_batteries+1
        for i in range(len(next_joltage)):
            #eliminate the extra battery and check max_joltage
            max_joltage=max(max_joltage,int(next_joltage[:i]+next_joltage[i+1:]))
    return max_joltage

def max_joltage_sum(size:int)-> int:
    jolt_banks=read_input()
    jolt_sum=0
    for jolt_bank in jolt_banks:
        result=max_joltage_for_bank(size,jolt_bank)
        jolt_sum+=result
    print(f'Total joltage for {size} batteries: {jolt_sum}')
    return jolt_sum

def main():
    max_joltage_sum(2)
    max_joltage_sum(12)

if __name__ == "__main__":
    main()
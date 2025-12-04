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

def max_joltage_sum(no_of_batteries:int)-> int:
    joltage_banks=read_input()
    total_joltage=0
    for joltage_bank in joltage_banks:
        max_joltage=max_joltage_for_bank(no_of_batteries,joltage_bank)
        total_joltage+=max_joltage
    print(f'Total joltage for {no_of_batteries} batteries: {total_joltage}')
    return total_joltage

def main():
    max_joltage_sum(2)
    max_joltage_sum(12)

if __name__ == "__main__":
    main()
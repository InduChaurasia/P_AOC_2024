"""AOC day 22: https://adventofcode.com/2024/day/22"""
from collections import deque,defaultdict
from utilities import read_file,Year

INITIAL_SECRETS=list(map(int,read_file(Year.y2024,'day22.txt')))
NUMBER_OF_SECRETS=2000

def calc_secret_num(secret_num):
    secret_num = ((secret_num * 64) ^ secret_num) % 16777216
    secret_num = ((secret_num // 32) ^ secret_num) % 16777216
    secret_num = ((secret_num * 2048) ^ secret_num) % 16777216
    return secret_num

def find_nth_secret(secret,n):
    for _ in range(n):
        secret = calc_secret_num(secret)
    return secret

def find_pattern_prices_for_secret(secret):
    pattern_prices={}
    recent_diffs = deque(maxlen=4)
    processed_patterns=set()
    for _ in range(NUMBER_OF_SECRETS):
        new_secret=calc_secret_num(secret)
        diff=new_secret%10-secret%10
        recent_diffs.append(diff)
        
        if len(recent_diffs)==4:
            pattern= ','.join(map(str,recent_diffs))
            if pattern not in processed_patterns:
                processed_patterns.add(pattern)
                pattern_prices[pattern]=new_secret%10
        secret=new_secret

    return pattern_prices

def find_pattern_price_for_all_secrets():
    aggregated_prices = defaultdict(int)
    for secret in INITIAL_SECRETS:
        curr_pattern_prices=find_pattern_prices_for_secret(secret)
        for pattern,price in curr_pattern_prices.items():
            aggregated_prices[pattern] += price
    return aggregated_prices

def find_max_price_pattern():
    pattern_prices=find_pattern_price_for_all_secrets()
    return max(pattern_prices.items(),key=lambda x:x[1])

def find_nth_secret_sum(n):
    return sum(find_nth_secret(secret,n) for secret in INITIAL_SECRETS)

def main():
    print(find_nth_secret_sum(NUMBER_OF_SECRETS))
    pattern,max_price=find_max_price_pattern()
    print(f'max_price: {max_price}, pattern:{pattern}')

if __name__=='__main__':
    main()

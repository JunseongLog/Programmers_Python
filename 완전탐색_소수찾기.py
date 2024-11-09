# 프로그래머스_완전탐색_소수찾기
from itertools import permutations

def isPrime(n):
    n = int(n)
    if n < 2:
        return False
    
    # 에라토스테네스의 체를 이용
    for i in range(2, int(n**(1/2))+1):
        if n % i == 0:
            return False
                   
    return True

def solution(numbers):
    # 소수 카운트
    cnt = 0
    # 순열 리스트
    permutation_list = []
                   
    for i in range(len(numbers)):
        permutation_list += list(map("".join, permutations(numbers, i+1)))
    
    # set()으로 중복을 없앤다
    permutation_list = [int(value) for value in permutation_list]
    permutation_list = set(permutation_list)

    
    for value in permutation_list:
        if isPrime(int(value)):
            cnt += 1
        
                   
    return cnt